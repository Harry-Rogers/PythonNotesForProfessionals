# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 12:26:18 2020

@author: Harry
"""

from requests import post
foo = post('http://natas0.natas.labs.overthewire.org', auth=('natas0', 'natas0'))
print(foo)

#same as below
from requests.auth import HTTPBasicAuth
foo = post('http://natas0.natas.labs.overthewire.org', auth=HTTPBasicAuth('natas0', 'natas0'))
print(foo)

