# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 14:38:23 2020

@author: Harry
"""

import requests

with requests.Session() as session:
    
    session.headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    
    session.get('http://httpbin.org/cookies/set?key=value')
    
    response = session.get('http://httpbin.org/cookies')
    
    print(response)
