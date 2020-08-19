# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 14:05:35 2020

@author: Harry
"""

d_empty = {}
d = {'key':'value'}
d_class = dict()
d['newkey'] = 42
d['new_list'] = [1,2,3]
d['new_dict'] = {'nested_dict':1}
print(d)
del d['newkey']
print(d)