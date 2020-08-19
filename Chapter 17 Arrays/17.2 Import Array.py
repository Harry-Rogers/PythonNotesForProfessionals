# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:39:09 2020

@author: Harry
"""

from array import *
my_array = array('i', [1,2,3,4,5])
for i in my_array:
    print(i)

my_array.append(6)
print(my_array)
my_array.insert(0,0)
print(my_array)
c = [11,12,13]
my_array.fromlist(c)
print(my_array)
print(my_array.index(0))
rev = my_array.reverse()
print(rev)
