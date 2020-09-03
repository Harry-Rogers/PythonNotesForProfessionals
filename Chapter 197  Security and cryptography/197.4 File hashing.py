# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 12:52:13 2020

@author: Harry
"""

import hashlib

hasher = hashlib.new('sha256')
with open('secretinfo.txt', 'r') as f:
    contents = f.read()
    contents.encode('utf-8')
    hasher.update(contents)
    
print(hasher.hexdigest())