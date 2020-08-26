# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 12:32:35 2020

@author: Harry
"""

from requests import post
proxies = {
    'http': 'http://192.168.0.128:3128',
    'https': 'http://192.168.0.127:1080',   
    }
foo = post('http://httpbin.org/post', proxies=proxies)
print(foo)
proxies = {'http': 'http://user:pass@192.168.0.128:312'}
foo = post('http://httpbin.org/post', proxies=proxies)
print(foo)

proxies = {
'http': 'socks5://user:pass@host:port',
'https': 'socks5://user:pass@host:port'
}

foo = post('http://httpbin.org/post', proxies=proxies)