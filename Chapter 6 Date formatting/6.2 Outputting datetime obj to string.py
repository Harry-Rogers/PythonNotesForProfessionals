# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 17:33:16 2020

@author: Harry
"""

from datetime import datetime
date_time_for_string = datetime.now()
datetime_string_format = "%d %b %Y, %H: %M: %S"
print(datetime.strftime(date_time_for_string, datetime_string_format))
