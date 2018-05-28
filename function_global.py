#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 13:05:34 2018

@author: osboxes
"""

x = 50

def func():
    global x
    
    print('x is', x)
    x = 2
    print('Changed global x to', x)

func()
print('Value of x is', x)
