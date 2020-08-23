# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 13:36:20 2020

@author: Harry
"""

import urllib
query_parms = {'username':'stackoverflow', 'password': 'me.me'}
encoded_parms = urllib.parse.urlencode(query_parms).encode('utf-8')
response = urllib.request.urlopen("https://stackoverflow.com/users/login", encoded_parms)
response.code
print(response.read())