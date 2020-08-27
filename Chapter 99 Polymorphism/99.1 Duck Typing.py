# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 12:37:08 2020

@author: Harry
"""

class Duck:
    def quack(self):
        print("Quack")
    def feathers(self):
        print("The duck has white feathers")

class Person:
    def quack(self):
        print("The person imitates a duck.")
    def feathers(self):
        print("The person takes a feather from the ground and shows it.")
    def name(self):
        print("John Smith")
        
def In_the_forest(obj):
    obj.quack()
    obj.feathers()

donald = Duck()
john = Person()
In_the_forest(donald)
In_the_forest(john)
       