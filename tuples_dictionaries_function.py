#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 19:59:38 2018

@author: osboxes
"""

def powersum(power, *args):
    '''Return the sum of each argument raised to the specified power.'''
    total = 0
    for i in args:
        total += pow(i, power)
    return total
print(powersum(2, 3, 4))
print(powersum(2, 10))
