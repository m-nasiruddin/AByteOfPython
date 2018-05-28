#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 16:20:14 2018

@author: osboxes
"""

def reverse(text):
    return text[::-1]
def is_palindrome(text):
    return text == reverse(text)
something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome.")
else:
    print("No, it is not a palindrome.")
