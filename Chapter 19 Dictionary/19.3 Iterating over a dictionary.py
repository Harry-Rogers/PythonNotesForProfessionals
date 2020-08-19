# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 16:05:23 2020

@author: Harry
"""

d = {'a':1, 'b':2, 'c':3}
for key in d:
    print(key, d[key])
#iterate and print key and values
print([key for key in d])
#print keys for dict
for key, value in d.items():
    print(key, value)
#same as first loop
