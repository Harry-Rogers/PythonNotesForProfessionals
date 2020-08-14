# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 17:18:27 2020

@author: Harry
"""

from datetime import datetime
a = datetime.now()
b = datetime(2016,10,1,23,59,59)
print("days since 1st oct 16: ", (a-b).days)