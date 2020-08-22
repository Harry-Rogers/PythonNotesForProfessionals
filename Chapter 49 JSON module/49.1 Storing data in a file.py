# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 11:57:14 2020

@author: Harry
"""

import json
d = {
     'foo':'bar',
     'alice':1,
     'wonderland':[1,2,3]
     }
with open('data', 'w') as f:
    json.dump(d,f)
    