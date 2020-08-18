# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 12:25:39 2020

@author: Harry
"""
i=0
while i <7:
    print(i)
    if i ==4:
        print("BreakBoi")
        break
    i +=1

for i in (0,1,2,3,4):
    print(i)
    if i==2:
        break
#break stops code 
        
for i in (0,1,2,3,4,5):
    if i ==2 or i ==4:
        continue
    print(i)
#continue stops print but keeps going instead of break

y = False
while y==True:
    for i in range (1,5):
        print(i)
        if i==2:
            break
#never ending loop as it will print 1 2 then break then go again as while is true
        
def break_loop():
    for i in range(1,5):
        if(i==2):
            return(i)
        print(i)
    return(5)
break_loop()
#returns 2 and prints 1
print("----------")
def break_all():
    for j in range(1,5):
        for i in range(1,4):
            if i*j ==6:
                return(i)
            print(i*j)

break_all()
#same as above but using a nested loop