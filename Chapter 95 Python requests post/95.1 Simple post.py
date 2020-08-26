# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 11:26:47 2020

@author: Harry
"""

from requests import post

foo = post('http://httpbin.org/post', data = {'key':'value'})
print(foo.headers)

print(foo.encoding)
foo.encoding = 'utf-8'
print(foo.encoding)

#Requests by default validates SSL certificates of domains. Overridden below
foo = post('http://httpbin.org/post', data = {'key':'value'}, verify=False)
print(foo) #200 all good

foo = post('http://httpbin.org/post', data = {'key':'value'}, allow_redirects = False)
print(foo.url)

print(foo.history)