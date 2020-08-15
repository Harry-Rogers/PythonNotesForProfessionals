# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:18:35 2020

@author: Harry
"""
import operator
a,b = 1,2
print(a+b)
print(operator.add(a,b))
#add is just add
a +=b
a = operator.iadd(a,b)
print(a)
#+= and iadd is a= a+b so 1+2 = 3

z = [1,2,3] + [4,5,6]
print(z)
#+ can also concatenate strings lists and tuples