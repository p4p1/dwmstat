#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Made by papi
# Created on: Fri 12 Jun 2020 11:37:06 PM CEST
# package.py
# Description:

import os

class Package:
    def __init__(self):
        self.packman = "pacman"
        self.pacman_path = "/var/lib/pacman/db.lck"
        self.delimeter = ('[', ']')
        self.pos = 0

    def is_running(self):
        if os.path.isfile(self.pacman_path):
            return True
        else:
            return False
    def __str__(self):
        if self.pos > 10:
            self.pos = 0
        fmt = " " + self.packman + ": " + self.delimeter[0]
        for i in range(0, self.pos):
            fmt += '='
        for i in range(self.pos, 10):
            fmt += ' '
        fmt += self.delimeter[1]
        self.pos += 1
        return (fmt)

if __name__ == "__main__":
    pac = Package()
    while pac.is_running():
        print(str(pac))
