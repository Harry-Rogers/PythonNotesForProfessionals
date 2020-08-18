# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 15:55:16 2020

@author: Harry
"""

class Foo(object):
    def __init__(self, item):
        self.my_item = item
    def __eq__(self, other):
        return self.my_item == other.my_item
    
a = Foo(5)
b = Foo(5)
print(a == b)
print(a !=b)
print(a is b)
#need to be same item