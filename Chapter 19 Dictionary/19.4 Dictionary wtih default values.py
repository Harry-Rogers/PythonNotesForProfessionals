# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 16:09:01 2020

@author: Harry
"""

from collections import defaultdict
d = defaultdict(int)
d['key']
d['key'] = 5
print(d['key'])

d = defaultdict(lambda: 'empty')
print(d['key'])
d['key'] = 'full'
print(d['key'])


d.setdefault('Another key', []).append("This worked")
print(d)