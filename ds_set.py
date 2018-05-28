#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 12:36:12 2018

@author: osboxes
"""

bri = set(['brazil', 'russia', 'india'])
'india' in bri
'usa' in bri
bric = bri.copy()
bric.add('china')
bric.issuperset(bri)
bri.remove('russia')
bri & bric # OR bri.intersection(bric)
{'brazil', 'india'}
