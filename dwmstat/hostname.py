#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Made by papi
# Created on: Wed 10 Jun 2020 04:01:37 PM CEST
# hostname.py
# Description:

class hostname:
    def __call__(self):
        with open("/etc/hostname", "r") as fp:
            return (" {}".format(fp.read().strip('\n')))
    def __str__(self):
        with open("/etc/hostname", "r") as fp:
            return ("[ {}]".format(fp.read().strip('\n')))
