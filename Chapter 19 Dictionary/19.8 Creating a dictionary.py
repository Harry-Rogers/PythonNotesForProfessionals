# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 16:31:35 2020

@author: Harry
"""

stock = {'eggs':5, 'milk':2}
dictionary = {}
dictionary['eggs'] = 5
dictionary['milk'] = 2

mydict = {'a': [1,2,3], 'b':['one', 'two', 'three']}

mydict['a'].append(4)
print(mydict)
mydict['b'].append('four')
print(mydict)

iterable = [('eggs',5),('milk',2)]
dictionary = dict(iterable)
print(dictionary)

dictionary = dict(eggs = 5, milk =2)
print(dictionary)

dictionary = dict.fromkeys(('milk', 'eggs'))
print(dictionary)

dictionary = dict.fromkeys(('milk', 'eggs'), (2,5))
print(dictionary)