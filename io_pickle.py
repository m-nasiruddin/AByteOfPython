#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 16:42:53 2018

@author: osboxes
"""

import pickle
# the name of the file where we'll store the object
shoplistfile = 'shoplist.data'
# the list of things to buy
shoplist = ['apple', 'mango', 'carrot']
# write to the file
f = open(shoplistfile, 'wb')
# dump the object to a file
pickle.dump(shoplist, f)
f.close()
# destroy the shoplist variable
del shoplist
# read back from the storage
f = open(shoplistfile, 'rb')
# load the object from the file
storedlist = pickle.load(f)
print(storedlist)
