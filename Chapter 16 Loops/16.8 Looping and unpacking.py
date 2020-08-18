# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:25:01 2020

@author: Harry
"""

collection = [('a', 'b', 'c'), ('x','y','z'), ('1','2','3')]

for item in collection:
    i1 = item[0]
    i2 = item[1]
    i3 = item[2]
    print(i1)
    print(i2)
    print(i3)

for i1, i2, i3 in collection:
    print(i1, i2, i3)
# does the same thing as above in less steps
    