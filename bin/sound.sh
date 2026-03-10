#!/bin/bash
# sound.sh
# Created on: Fri 12 Jun 2020 03:01:16 PM CEST
#
#  ____   __  ____  __
# (  _ \ /. |(  _ \/  )
#  )___/(_  _))___/ )(
# (__)    (_)(__)  (__)
#
# Description:
#  Sound update script for the status bar
#
# Usage:
#  ./sound.sh +  -> increment brightness by 0.1
#  ./sound.sh -  -> decrease brightness by 0.1
#  ./sound.sh =  -> set brightness to 1

pid=$(ps aux | grep "dwmstat" | head -n1 | awk -F' ' '{print $2}')

get_volume() {
    amixer sget Master | grep -o '[0-9]*%' | head -1 | tr -d '%'
}

get_icon() {
    local vol=$1
    if [ "$vol" -le 33 ]; then
        echo "audio-volume-low"
    elif [ "$vol" -le 66 ]; then
        echo "audio-volume-medium"
    else
        echo "audio-volume-high"
    fi
}

if [ "$1" = "-" ]; then
	amixer set Master 5%- && kill -s SIGUSR1 $pid
	vol=$(get_volume)
	icon=$(get_icon $vol)
	notify-send -i "$icon" \
		-h int:value:$vol \
		-h string:synchronous:volume \
		"Volume" "${vol}%"
fi
if [ "$1" = "+" ]; then
	amixer set Master 5%+ && kill -s SIGUSR1 $pid
	vol=$(get_volume)
	icon=$(get_icon $vol)
	notify-send -i "$icon" \
		-h int:value:$vol \
		-h string:synchronous:volume \
		"Volume" "${vol}%"

fi
if [ "$1" = "=" ]; then
	amixer set Master toggle && kill -s SIGUSR1 $pid
	notify-send -i "audio-volume-muted" \
		-h string:synchronous:volume \
		"Volume" "Muted"

fi
