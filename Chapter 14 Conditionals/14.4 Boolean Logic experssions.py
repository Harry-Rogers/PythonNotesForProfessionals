# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 15:14:49 2020

@author: Harry
"""

print(1 and 2)

print(1 and 0)

print(1 and "Hello world")

print("" and "pancackes")

#and both have to be true so if empty (last case) will be false so no print

print(1 or 2)

print(None or 1)

print(0 or [])
#prints true value or last value

#could do
def print_me():
    print("HERE")
print(0 and print_me())
#lazy eval 

a = 1
b = 6
if a and b >2:
    print("yes")
else:
    print("No")

#case one is no so no seperate to correctly print
if a >2 and b >2:
    print("yes")
else:
    print("no")
    
if a==3 or 4 or 6:
    print("yes")
else:
    print("no")
#again needs to be evaluated properly otherwise incorrect

if a ==3 or a==4 or a==6:
    print("yes")
else:
    print("no")
# need to seperate othwerwise it will be evaluated wrong
    
if a in(3,4,6):
    print("yes")
else:
    print("no")
#can use in for ==