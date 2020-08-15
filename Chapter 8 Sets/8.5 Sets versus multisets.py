# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:04:07 2020

@author: Harry
"""
#sets ignore duplicates
setA = {"a","b","b","c"}
print(setA)
listA = ["a","b","b","c"]
print(listA)

from collections import Counter
counterA = Counter(["a","b","b","c"])
print(counterA)