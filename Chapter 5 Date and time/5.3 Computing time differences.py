# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 16:22:29 2020

@author: Harry
"""

from datetime import datetime, timedelta
now = datetime.now()
then = datetime(2016, 5, 23)
delta = now - then
print(delta.days)
#days since 23/5/2016
print(delta.seconds)
#secods since 23/5/2016

def get_n_days_after_today(date_format = "%d %B %y", add_days = 120):
    date_n_days_after = datetime.datetime.now() + timedelta(days = add_days)
    return date_n_days_after.strftime(date_format)
# adds 120 days to the date
    