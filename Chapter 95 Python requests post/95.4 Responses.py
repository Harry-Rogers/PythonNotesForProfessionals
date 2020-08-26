# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 12:19:34 2020

@author: Harry
"""

from requests import post
foo = post('http://httpbin.org/post', data={'data' : 'value'})
print(foo.status_code)
print(foo.text)
res = foo.raw
print(res.read())