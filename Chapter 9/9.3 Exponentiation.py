# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 16:23:01 2020

@author: Harry
"""

a,b,c =2,3,2
c = (a**b)
print(c)
print(pow(a,b))
print(pow(a,b,c))
#pow can use 3 arguments insterad of 2 with math.pow
import math
print(math.pow(a,b))
#math.pow uses the float instead of int
import operator
print(operator.pow(a,b))
# operator uses int

import cmath
c = 4
print(math.sqrt(c))
print(cmath.sqrt(c))
#math sqrt shows as long instead of float

x = 8
print(math.pow(x, 1/3))
print(x**(1/3))

print(math.exp(0))
print(math.exp(1))
#exponential

print(math.exp(1e-6)-1)
print(math.expm1(1e-6))
#second use of expm1 is much more accurate when using smaller vals