# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 12:50:50 2020

@author: Harry
"""

import hashlib
h = hashlib.new('sha256')
h.update(b'Nobody expects the Spanish Inquisition.')
span = h.digest()
print(span)