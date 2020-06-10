#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Made by papi
# Created on: Wed 10 Jun 2020 02:42:07 PM CEST
# date_time.py
# Description:

from time import gmtime, strftime

class dateandtime:
    def __call__(self):
        return (strftime("%d/%m/%Y %H:%M", gmtime()))
    def __str__(self):
        return ("[{}]".format(strftime("%d/%m/%Y %H:%M", gmtime())))
