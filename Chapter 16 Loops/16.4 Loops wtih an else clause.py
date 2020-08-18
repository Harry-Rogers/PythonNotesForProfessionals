# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 13:14:13 2020

@author: Harry
"""

for i in range(3):
    print(i)
else:
    print("Done")
    
i = 0

while i < 3:
    print(i)
    i +=1
else:
    print("Done")

for i in range(2):
    print(i)
    if i ==1:
        break
else:
    print("Done")
    
a = [1,2,3,4]
for i in a:
    if type(i) is not int:
        print(i)
        break
else:
    print("No exception")
