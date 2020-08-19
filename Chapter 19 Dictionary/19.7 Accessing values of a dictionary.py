# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 16:27:43 2020

@author: Harry
"""

dictionary = {"Hello": 1234, "World":5678}
print(dictionary["Hello"])
w = dictionary.get("Whatever")
x = dictionary.get("Whatever", "nuh-uh")
print(w)
print(x)