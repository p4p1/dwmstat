#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Made by papi
# Created on: Wed 10 Jun 2020 01:14:46 PM CEST
# battery.py
# Description:

import os
from os import listdir
from .color import *

class Battery:
    def __init__(self):
        self.directory = "/sys/class/power_supply"
        self.animation = ""
        self.charging_icon = ""
        self.is_plugged = False

    def __str__(self):
        return "[{}]".format(self.main())

    def plugged(self):
        with open(self.directory + "/AC/online", "r") as fp:
            if "1" in fp.read():
                return True
            else:
                return False

    def percentage(self, fp):
        fmt = ""

        with open(self.directory + "/" + fp + "/capacity", "r") as bat:
            pe = int(bat.read().strip("\n"))
            pos = int(len(self.animation) * pe / 100)
            if pe < 20:
                fmt += red(pe)
            elif pe < 45:
                fmt += orange(pe)
            else:
                fmt += str(pe)
            fmt += self.animation[pos]
        return fmt

    def main(self):
        fmt = ""

        if self.plugged():
            fmt += "{} ".format(purple(self.charging_icon))
        for fp in listdir(self.directory):
            if "AC" in fp:
                continue
            else:
                fmt += self.percentage(fp)
        return (fmt)

if __name__ == "__main__":
    bat = Battery()

    print(bat.plugged())
    print(str(bat))
    os.system("xsetroot -name \"{}                      \"".format(str(bat)))
