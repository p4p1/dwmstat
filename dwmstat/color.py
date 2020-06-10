#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Made by papi
# Created on: Wed 10 Jun 2020 01:16:14 PM CEST
# color.py
# Description:
#  Put the text in color

import os

def purple(st):
    return ("\x02{}\x01".format(st))

def blue(st):
    return ("\x05{}\x01".format(st))

def orange(st):
    return ("\x03{}\x01".format(st))

def red(st):
    return ("\x04{}\x01".format(st))

def green(st):
    return ("\x06{}\x01".format(st))

if __name__ == "__main__":
    fmt = "{} {} {} {} {} [normal]".format(green("[ok]"), blue("[custom]"),
        red("[urgent]"), orange("[warning]"), purple("[selected]"))
    os.system("xsetroot -name \"{}\"".format(fmt))
