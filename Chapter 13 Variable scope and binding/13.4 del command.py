# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 18:47:55 2020

@author: Harry
"""

x = 5
print(x)
del x
#print(x)
#deletes x after call 

class A:
    pass
a = A()
a.x = 7
print(a.x)
#del a.x
#print(a.x)
#delete elements of a class that was created

y = {'a':1,'b':2}
del y['a']
print(y['b'])
#can delete specific vals or entire thing
