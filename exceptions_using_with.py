#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 18:29:28 2018

@author: osboxes
"""

with open("poem.txt") as f:
    for line in f:
        print(line, end='')
