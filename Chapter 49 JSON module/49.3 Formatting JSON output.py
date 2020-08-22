# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 12:06:02 2020

@author: Harry
"""

import json
data = {"cats": [{"name": "Tubbs", "color": "white"}, {"name": "Pepper", "color": "black"}]}
print(json.dumps(data))
#big dump
print(json.dumps(data, indent =2))
#formatted dump
print(json.dumps(data, sort_keys=True))
#alphabetical order
print(json.dumps(data, separators = (',',':')))
