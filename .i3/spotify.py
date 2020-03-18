#!/bin/python
import dbus
from subprocess import check_output, call
import os

def parseButton(button, interface):
    if button == "1": #PlayPause
        interface.PlayPause()
    elif button == "2": #Previous
        interface.Previous()
    elif button == "3": #Next
        interface.Next()
    elif button == "4":
        changeVolume(5)
    elif button == "5":
        changeVolume(-5)

def changeVolume(amm):
    amm_s = ""
    if amm > 0:
        amm_s = str(amm)+"%+"
    else:
        amm_s = str(-amm)+"%-"
    call(("amixer -q -D default sset Master "+amm_s+" unmute").split(" "))

def printStatusIcon(status_song):
    if status_song == "Paused":
        print("", end='')
    elif status_song == "Playing":
        print("", end='')
    elif status_song == "Stopped":
        print("", end='')

if __name__ == '__main__':
    bus = dbus.SessionBus()
    proxy = bus.get_object('org.mpris.MediaPlayer2.spotify', '/org/mpris/MediaPlayer2')
    interface = dbus.Interface(proxy, 'org.mpris.MediaPlayer2.Player')
    props_iface = dbus.Interface(proxy, dbus_interface='org.freedesktop.DBus.Properties')
    infos = props_iface.GetAll("org.mpris.MediaPlayer2.Player")['Metadata']
    artist = str(infos['xesam:artist'][0])
    album = str(infos['xesam:album'])
    title = str(infos['xesam:title'])
    status = str(props_iface.GetAll("org.mpris.MediaPlayer2.Player")['PlaybackStatus'])
    button = os.environ["BLOCK_BUTTON"]
    parseButton(button, interface)
    printStatusIcon(status)
    print(" %s - %s" % (artist, title))
