# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 18:26:35 2020

@author: Harry
"""

def counter():
    num = 0
    def incrementer():
        num +=1
        return print(num)
    return print(incrementer)
counter()

#above code has nonlocal error as num is not declared in the correct func

def counter_():
    num = 0
    def incrementer_():
        nonlocal num
        num+=1
        return print(num)
    return print(incrementer_)
counter_()
#runs either way assumed python upadtes fix this :|