# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 12:36:16 2020

@author: Harry
"""

import hashlib
import os

salt = os.urandom(16)
hash = hashlib.pbkdf2_hmac('sha256', b'password', salt, 100000)
print(hash)