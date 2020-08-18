# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:07:01 2020

@author: Harry
"""

for x in ['one', 'two', 'three', 'four']:
    print(x)
#prints the list items

for x in range(1,6):
    print(x)

for index, item in enumerate(['one','two','three','four']):
    print(index, "::", item)
#enumerate allows for both elements so we can have index and item