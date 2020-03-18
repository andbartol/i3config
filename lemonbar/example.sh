#!/usr/bin/bash

# Define the clock
Clock() {
        DATETIME=$(date "+%a %b %d, %T")

        echo -n "$DATETIME"
}

# Print the clock

while true; do
        echo "%{r}%{F#FFFFFF}%{B#000000}%{A1:ciao:} $(Clock) %{A}%{F#0000FF00}%{B#0000FF00}%{S0}"
        sleep 1
done
