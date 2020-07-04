#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Made by papi
# Created on: Wed 10 Jun 2020 04:31:02 PM CEST
# sound.py
# Description:

import alsaaudio
from .color import *

class Sound:
    def main(self):
        m = alsaaudio.Mixer()
        if  m.getmute()[0] == 1:
            return ("  ")
        else:
            return "{}%".format(m.getvolume()[0])
    def __call__(self):
        return self.main()
    def __str__(self):
        return "[{}]".format(self.main())

if __name__ == "__main__":
    print (Sound())
