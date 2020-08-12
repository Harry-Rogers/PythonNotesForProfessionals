# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 15:05:45 2020

@author: Harry
"""

basket = {"apple","orange","apple","pear","bannana"}
print(basket)
#duplicates from a set are removed on print
a = set("abracadabra")
print(a)
# prints the unique letters in a 
a.add("z")
print(a)
#can add to a set but will be at the start of the set

b = frozenset("asdfgasa")
print(b)
# cant add to a frozen set 