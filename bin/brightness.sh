#!/bin/bash
# brightness.sh
# Created on: Mon 15 Jun 2020 02:17:45 AM CEST
#
#  ____   __  ____  __
# (  _ \ /. |(  _ \/  )
#  )___/(_  _))___/ )(
# (__)    (_)(__)  (__)
#
# Description:
#  Brightness update script for the status bar
#
# Usage:
#  ./brightness.sh +  -> increment brightness by 0.1
#  ./brightness.sh -  -> decrease brightness by 0.1
#  ./brightness.sh =  -> set brightness to 1

pid=$(ps aux | grep "dwmstat" | head -n1 | awk -F' ' '{print $2}')
brightness=$(brightnessctl -m | cut -d, -f4 | tr -d '%')


if [ "$1" = "+" ]; then
	brightnessctl s +10%
	notify-send -h int:value:$brightness -h string:synchronous:brightness " Brightness" "${brightness}%"

	kill -s SIGUSR2 $pid
fi
if [ "$1" = "-" ]; then
	brightnessctl s 10%-
	notify-send -h int:value:$brightness -h string:synchronous:brightness " Brightness" "${brightness}%"
	kill -s SIGUSR2 $pid
fi
if [ "$1" = "=" ]; then
	brightnessctl s 100%
	notify-send -h int:value:$brightness -h string:synchronous:brightness " Brightness" "${brightness}%"
	kill -s SIGUSR2 $pid
fi
