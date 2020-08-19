# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 16:40:38 2020

@author: Harry
"""

from collections import OrderedDict
d = OrderedDict()
d['first'] = 1
d['second'] = 2
d['third'] = 3
d['last'] = 4
for key in d:
    print(key, d[key])
