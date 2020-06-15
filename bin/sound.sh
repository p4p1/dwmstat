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

if [ "$1" = "-" ]; then
	amixer set Master 5%- && kill -s SIGUSR1 $pid
fi
if [ "$1" = "+" ]; then
	amixer set Master 5%+ && kill -s SIGUSR1 $pid
fi
if [ "$1" = "=" ]; then
	amixer set Master toggle && kill -s SIGUSR1 $pid
fi
