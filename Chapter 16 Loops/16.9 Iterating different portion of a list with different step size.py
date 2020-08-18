# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:30:08 2020

@author: Harry
"""

lst = ['alpha','bravo','charlie','delta','echo']
for s in lst:
    print(s[:1])

for idx, s in enumerate(lst):
    print("%s has an index of %d" %(s, idx))

for i in range(2,4):
    print("lst at %d contains %s" % (i, lst[i]))

#below code is the same output
for s in lst[1::2]:
    print(s)
    
for i in range(1, len(lst), 2):
    print(lst[i])