# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 16:07:35 2020

@author: Harry
"""

from datetime import datetime, timedelta, timezone
JST = timezone(timedelta(hours= +9))
#japan standard time 9 hrs ahead of gmt
dt = datetime(2015, 1, 1, 12, 0, 0, tzinfo = JST)
#call datetime from 1/1/15 for japan
print(dt)
print(dt.tzname())
#show timezone diff

dt = datetime(2015, 1, 1, 12, 0, 0, tzinfo = timezone(timedelta(hours = 9), 'JST'))
print(dt.tzname())
# show name given

#daylight savings use dateutil 
from dateutil import tz
local = tz.gettz()
PT = tz.gettz('US/Pacific')

dt_l = datetime(2015, 1, 1, 12, tzinfo= local)
dt_pst = datetime(2015, 1, 1, 12, tzinfo= PT)
dt_pdt = datetime(2015,7,1,12, tzinfo= PT)

print(dt_l) 
print(dt_pst) 
#shows before daylight savings
print(dt_pdt)
#after daylight savings 
# all dependent on date