# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 12:16:21 2020

@author: Harry
"""

from requests import post
files = {'file': open('data.txt', 'rb')}
foo = post('http://http.org/post', files=files)

multiple_files = [
 ('images', ('foo.png', open('foo.png', 'rb'), 'image/png')),
 ('images', ('bar.png', open('bar.png', 'rb'), 'image/png'))]

foo = post('http://httpbin.org/post', files=multiple_files)
#HTTPConnnectionPool error
