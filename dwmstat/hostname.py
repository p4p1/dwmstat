#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Made by papi
# Created on: Wed 10 Jun 2020 04:01:37 PM CEST
# hostname.py
# Description:
#            

import distro

class hostname:
    def main(self, fp):
        dist = distro.id()
        logo = ""

        if dist == "arch":
            logo = ""
        elif dist == "fedora":
            logo = ""
        elif dist == "ubuntu":
            logo = ""
        elif dist == "opensuse":
            logo = ""
        elif dist == "manjaro":
            logo = ""
        elif dist == "gentoo":
            logo = ""
        elif dist == "rhel":
            logo = ""
        elif dist == "centos":
            logo = ""
        elif dist == "debian":
            logo = ""
        elif dist == "linuxmint":
            logo = ""
        return ("{} {}".format(logo, fp.read().strip('\n')))
    def __call__(self):
        with open("/etc/hostname", "r") as fp:
            return (self.main(fp))
    def __str__(self):
        with open("/etc/hostname", "r") as fp:
            return ("[{}]".format(self.main(fp)))
