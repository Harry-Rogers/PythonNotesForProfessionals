# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 17:10:36 2020

@author: Harry
"""

import datetime

today = datetime.date.today()
print("Today: " ,today)

yesterday = today - datetime.timedelta(days = 1)
print("Yesterday: " ,yesterday)

tommorrow = today + datetime.timedelta( days = 1)
print("Tomorrow: ", tommorrow)
