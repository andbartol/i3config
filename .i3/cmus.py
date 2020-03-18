#!/bin/python
from subprocess import check_output, call
import os
import re

def getTag(status, search):
    for tag in status:
        if re.match(search, tag):
            break
    else:
        return "Unknown"
    words = len(search.split(" "))
    return " ".join(tag.split(" ")[words:])
def getTitle(status):
    return getTag(status, "tag title")
def getArtist(status):
    return getTag(status, "tag artist")
def getStatusSong(status):
    return getTag(status, "status")
def getFileName(status):
    return re.sub(r"/.*/(.*)\..*", r"\1", getTag(status, "file"))
def getStatus():
    status = callCmus("-Q")
    status = status.decode("utf-8")
    return status.split("\n")

def callCmus(args):
    return check_output(("cmus-remote --server 127.0.0.1:3000 --passwd nonteladico " + args).split(" "))
def cmusNext():
    callCmus("-n")
def cmusPrev():
    callCmus("-r")
def cmusPause():
    callCmus("-u")
def cmusPlay():
    callCmus("-p")

def changeVolume(amm):
    amm_s = ""
    if amm > 0:
        amm_s = str(amm)+"%+"
    else:
        amm_s = str(-amm)+"%-"
    call(("amixer -q -D default sset Master "+amm_s+" unmute").split(" "))

def parseButton(button, status_song):
    if button == "1":
        if status_song == "paused" or status_song == "stopped":
            cmusPlay()
        elif status_song == "playing":
            cmusPause()
    elif button == "2":
        cmusPrev()
    elif button == "3":
        cmusNext()
    elif button == "4":
        changeVolume(5)
    elif button == "5":
        changeVolume(-5)

def printStatusIcon(status_song):
    if status_song == "paused":
        print("", end='')
    elif status_song == "playing":
        print("", end='')
    elif status_song == "stopped":
        print("", end='')
def printInfo(artist, title, status, status_song):
    printStatusIcon(status_song)
    if artist != "Unknown" or title != "Unknown":
        print(" "+artist+" - "+title)
    else:
        print(" "+ getFileName(status))

if __name__ == '__main__':
    status = getStatus();
    status_song = getStatusSong(status)
    artist = getArtist(status)
    title = getTitle(status)
    button = os.environ["BLOCK_BUTTON"]

    parseButton(button, status_song)
    printInfo(artist, title, status, status_song)
