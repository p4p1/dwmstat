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
current_display_name=$(xrandr -q | grep ' connected' | head -n 1 | cut -d ' ' -f1)
current_brightness=$(xrandr --current --verbose | grep "Brightness" | cut -d':' -f2)

if [ "$1" = "+" ]; then
	brightness=$(echo "$current_brightness + 0.1" | bc)
	[ ! $brightness = "1.00" ] && xrandr --output $current_display_name --brightness $brightness
	kill -s SIGUSR2 $pid
fi
if [ "$1" = "-" ]; then
	brightness=$(echo "$current_brightness - 0.1" | bc)
	[ ! $brightness = "0" ] && xrandr --output $current_display_name --brightness $brightness
	kill -s SIGUSR2 $pid
fi
if [ "$1" = "=" ]; then
	xrandr --output $current_display_name --brightness 1
	kill -s SIGUSR2 $pid
fi
