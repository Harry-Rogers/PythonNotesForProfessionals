# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 13:30:08 2020

@author: Harry
"""

import urllib.request
stackoverflow = "http://stackoverflow.com"
print(urllib.request.urlopen(stackoverflow))
response = urllib.request.urlopen(stackoverflow)
print(response.code)
print(response.read())