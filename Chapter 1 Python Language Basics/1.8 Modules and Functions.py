# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 14:27:15 2020

@author: Harry
"""

print(dir(__builtins__)) 
# built in modules using dir 
help(max)
# help shows the funcitonality of the moudle used

import math
print(dir(math))
# import module then check what the classes are called that can be used.
help(math.fabs)
# help for module and the functionality of a class

print(math.__doc__)