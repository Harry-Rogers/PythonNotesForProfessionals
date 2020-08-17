# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 15:00:19 2020

@author: Harry
"""

a = 'global'

class Fred:
    a = 'class'
    b = (a for i in range(10)) # function scope
    c = [a for i in range(10)] # function scope
    d = a # class scope
    e = lambda: a # function scope
    f = lambda a=a: a # default argument uses class scope
    @staticmethod
    def g():
          return a
      
print(Fred.a)
print(next(Fred.b))
print(Fred.c[0]) 
print(Fred.d) 
print(Fred.e()) 
print(Fred.f())
print(Fred.g())