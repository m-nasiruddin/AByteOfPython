#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 12:26:59 2018

@author: osboxes
"""

class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print('hello, my name is', self.name)
Person('Nasir').say_hi()
# OR
p = Person('Nasir')
p.say_hi()
