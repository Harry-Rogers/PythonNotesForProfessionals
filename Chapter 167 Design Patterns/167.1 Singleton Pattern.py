# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 15:25:54 2020

@author: Harry
"""

class Singleton(object):
    def __new__(cls):
 # hasattr method checks if the class object an instance property or not.
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            return cls.instance
s = Singleton()
print ("Object created", s)
s1 = Singleton()
print ("Object2 created", s1)