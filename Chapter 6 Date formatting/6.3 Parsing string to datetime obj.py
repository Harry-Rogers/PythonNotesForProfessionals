# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 17:35:33 2020

@author: Harry
"""

from datetime import datetime
datetime_string = 'Oct 1 2016, 00:00:00'
datetime_string_format = '%b %d %Y, %H:%M:%S'
print(datetime.strptime(datetime_string, datetime_string_format))