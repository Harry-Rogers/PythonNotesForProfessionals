# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 18:37:07 2020

@author: Harry
"""

x = "Hi"

def read_x():
    print(x)

read_x()

def read_y():
    y = "hey"
    print(y)

read_y()

def read_local_x():
    x = "Bye"
    print(x)

read_local_x()
#can use local same var names for different vals/str to the global ones 

def change_global_x():
    global x
    x = "Changed"
    print(x)
change_global_x()
print(x)
#changes global and keeps change