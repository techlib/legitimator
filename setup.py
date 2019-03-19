#!/usr/bin/python3 -tt

from setuptools import setup
import os.path

setup(
    name = 'legitimator',
    version = '1',
    author = 'NTK',
    description = ('API for getting EKV group'),
    license = 'MIT',
    keywords = 'api ekv',
    include_package_data = True,
    package_data = {
        '': ['*.png', '*.js', '*.html'],
    },
    packages = [
        'legitimator',
    ],
    classifiers = [
        'License :: OSI Approved :: MIT License',
    ],
    scripts = ['legitimator-daemon']
)


# vim:set sw=4 ts=4 et:
# -*- coding: utf-8 -*-
