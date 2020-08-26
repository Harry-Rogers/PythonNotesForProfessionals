# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 11:50:37 2020

@author: Harry
"""

from requests import post

payload = {'key1' : 'value1',
           'key2' : 'value2'
           }
foo = post('http://httpbin.org/post', data=payload)
