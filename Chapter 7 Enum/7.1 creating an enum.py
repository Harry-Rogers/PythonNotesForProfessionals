# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 17:36:34 2020

@author: Harry
"""

from enum import Enum
class color(Enum):
    red = 1
    green = 2
    blue = 3

print(color.red)
print(color(1))
print(color['red'])
#enums?