# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 17:39:17 2020

@author: Harry
"""
from enum import Enum
class color(Enum):
    red = 1
    green = 2
    blue = 3
print([c for c in color])
#can iterate through all to find values 