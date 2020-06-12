#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Made by papi
# Created on: Wed 10 Jun 2020 12:56:28 PM CEST
# setup.py
# Description:

from setuptools import setup
with open("README.org", "r") as fh:
    long_description = fh.read()

setup(name='status',
    version='0.1',
    long_description=long_description,
    long_description_content_type="text/org",
    description='A status bar for dwm',
    url='https://p4p1.github.io/',
    author='p4p1',
    author_email='p4p1@vivaldi.net',
    license='GPL V3',
    packages=['dwmstat'],
    install_requires=[
        'pyalsaaudio',
        'distro',
    ],
    scripts=['bin/dwmstat',
             'bin/sound.sh'],
    zip_safe=False
)
