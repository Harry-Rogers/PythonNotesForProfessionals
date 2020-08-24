# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 16:50:58 2020

@author: Harry
"""

from urllib.request import urlopen
response = urlopen('http://stackoverflow.com/questions?sort=votes')
data = response.read()
#decode data 
encoding = response.info().get_content_charset()
html = data.decode(encoding)

print(html)