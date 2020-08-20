# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 11:22:06 2020

@author: Harry
"""

import collections
counts = collections.Counter([1,2,3])
print(counts)
print(counts[2])
#prints the number of 2's in the array
letters = collections.Counter('Happy Birthday')
print(letters)
print(letters['a'])
#same as above but with letters
words = collections.Counter('this that the other this that the other test-part test-part'.split())
print(words)
print(words['this'])
#same as the above but with words