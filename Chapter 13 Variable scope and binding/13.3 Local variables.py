# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 18:45:41 2020

@author: Harry
"""

def foo():
    if True:
        a = 5
    print(a)
#cant print a here as outside func

b = 3
def bar():
    if False:
        b = 5
    print(b)
