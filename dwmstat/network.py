#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Made by papi
# Created on: Wed 10 Jun 2020 02:52:11 PM CEST
# network.py
# Description:

import socket
import fcntl
import struct
import os

class Network:

    def get_ip_address(self, ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915,
            struct.pack('256s', ifname[:15]))[20:24])

    def __str__(self):
        return ("[{}]".format(self.main()))

    def main(self):
        devices = os.listdir("/sys/class/net")
        fmt = ""
        i = 0

        for dev in devices:
            if dev == "lo":
                continue
            else:
                if i != 0:
                    fmt += " "
                fmt += self.get_ip_address(bytes(dev, 'UTF-8'))
            i += 1
        return fmt

if __name__ == "__main__":
    net = Network()
    print(str(net))
