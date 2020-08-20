# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 11:52:39 2020

@author: Harry
"""

from collections import deque
d = deque('ghi')
for elem in d:
    print(elem.upper())
    #print elements in uppercase
d.append('i')
d.appendleft('f')
print(d)
print(d.pop())
print(d.popleft())

