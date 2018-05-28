#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 16:58:50 2018

@author: osboxes
"""

# encoding=utf-8
import io

f = io.open("abc.txt", "wt", encoding="utf-8")
f.write(u"Imagine non-English language here.")
f.close()
text = io.open("abc.txt", encoding="utf-8").read()
print(text)
