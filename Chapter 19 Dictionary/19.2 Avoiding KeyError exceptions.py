# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 16:00:18 2020

@author: Harry
"""

mydict = {}
#mydict['not there']
print(mydict)
print(mydict.get("foo","bar"))
print(mydict)
print(mydict.setdefault("foo", "bar"))
print(mydict)

#exception handling below
default_value = 1
try:
    value = mydict[key]
except KeyError:
    value = default_value
    
