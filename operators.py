#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 11:53:06 2018

@author: osboxes
"""

# + (plus) : adds two objects
print(3 + 5)
print('a' + 'b')
# - (minus): gives the subtraction of one number from the other; if the first
# operand is absent it is assumed to be zero
print(-5.2)
print(50 - 24)
# * (multiply): gives the multiplication of the two numbers or returns the
# string repeated that many times
print(2 * 3)
print('la' * 3)
# ** (power): returns x to the power of y
print(3 ** 4)
# / (divide): divide x by y
print(13 / 3)
# // (divide and floor): divide x by y and round the answer down to the nearest
# integer value. Note that if one of the values is a float, you'll get back a
# float
print(13 // 3)
print(-13 // 3)
print(9//1.81)
# % (modulo): returns the remainder of the division
print(13 % 3)
print(-25.5 % 2.25)
# << (left shift): shifts the bits of the number to the left by the number of
# bits specified. (Each number is represented in memory by bits or binary
# digits i.e. 0 and 1)
print(2 << 2)
# >> (right shift): shifts the bits of the number to the right by the number of
# bits specified
print(11 >> 1)
# & (bit-wise AND): bit-wise AND of the numbers
print(5 & 3)
# | (bit-wise OR): bitwise OR of the numbers
print(5 | 3)
# ^ (bit-wise XOR): bitwise XOR of the numbers
print(5 ^ 3)
# ~ (bit-wise invert): the bit-wise inversion of x is -(x+1)
print(~5)
# < (less than): returns whether x is less than y. All comparison operators
# return True or False
print(5 < 3)
print(3 < 5 < 7)
# > (greater than): returns whether x is greater than y
print(5 > 3)
# <= (less than or equal to): returns whether x is less than or equal to y
print(3 <= 6)
# >= (greater than or equal to): peturns whether x is greater than or equal to y
print(4 >= 3)
# == (equal to): compares if the objects are equal
print( 2 == 2)
print('str' == 'stR')
print('str' == 'str')
# != (not equal to): compares if the objects are not equal
print(2 != 3)
# not (boolean NOT)
print(not False)
# and (boolean AND)
print(False and True)
# or (boolean OR)
print(True or False)

a = 2
a = a * 3
print(a)
a = 2
a *= 3
print(a)