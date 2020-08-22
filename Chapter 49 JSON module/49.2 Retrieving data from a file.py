# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 12:04:35 2020

@author: Harry
"""

import json
with open('data', 'r') as f:
    d = json.load(f)
    print(d)