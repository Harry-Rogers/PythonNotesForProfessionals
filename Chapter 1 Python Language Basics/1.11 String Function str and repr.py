# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 14:52:09 2020

@author: Harry
"""

s = """w'o'w"""
print(repr(s))
print(str(s))
#repr shows everything in the string whereas str shows human readable string

import datetime
today = datetime.datetime.now()
print(repr(today))
print(str(today))
# another example