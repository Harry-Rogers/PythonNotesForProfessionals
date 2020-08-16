# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 18:08:35 2020

@author: Harry
"""

x = True
y = True
z = False
w = x and y
print(w)
#true and true = true
q = x and z
print(q)
#true and false = false
print(q and z)
#false and false = false