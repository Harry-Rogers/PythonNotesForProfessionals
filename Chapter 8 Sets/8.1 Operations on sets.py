# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 12:09:13 2020

@author: Harry
"""
a = {1,2,3,4,5}
print(a.intersection({3,4,5}))
print(a&{3,4,5,6})
#Intersection and & is to check if second set elements are in first

print(a.union({3,4,5,6}))
print(a|{3,4,5,6})
#Union and | joins the two sets

print(a.difference({2,3,5}))
print(a-{2,3,5})
#difference and - are what is different from set 1 to set 2

print({1,2,3,4}.symmetric_difference({2,3,5}))
print({1,2,3,4}^{2,3,5})
#symmetric difference and ^ are whats different in each set

print({1, 2}.issuperset({1, 2, 3})) 
print({1, 2} >= {1, 2, 3})
#superset or >= checks if all elements are in second set 

print({1, 2}.issubset({1, 2, 3}))
print({1, 2} <= {1, 2, 3})
#subset or <= checks if elements are a part of second set

print({1, 2}.isdisjoint({3, 4}))
print({1, 2}.isdisjoint({1, 4}))
#isdisjoint is a check to see if any elements are in second set

print(2 in {1,2,3})
print(4 in {1,2,3})
print(4 not in {1,2,3})

print(a.add(6))
print(a)
a.discard(4)
print(a)
a.remove(1)
print(a)
a.update({1,4})
print(a)
