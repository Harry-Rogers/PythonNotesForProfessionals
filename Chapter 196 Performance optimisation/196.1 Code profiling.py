# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 12:29:30 2020

@author: Harry
"""

import cProfile

def f(x):
    return x/2
cProfile.run('f(7)')

#use this and unit tests to optimise code for speed and accuracy