#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Made by papi
# Created on: Wed 10 Jun 2020 02:42:07 PM CEST
# date_time.py
# Description:

import datetime

class dateandtime:
    def __call__(self):
        x = datetime.datetime.now()
        return (x.strftime("%b %d %Y %H:%M"))
    def __str__(self):
        x = datetime.datetime.now()
        return ("[{}]".format(x.strftime("%b %d %Y %H:%M")))
