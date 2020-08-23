# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 11:57:21 2020

@author: Harry
"""

import urllib.request
site = "http://stackoverflow.com/"
response  = urllib.request.urlopen(site)
data = response.read()

encoding  = response.info().get_content_charset()
html = data.decode(encoding)
print(html)
