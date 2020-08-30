# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 15:34:54 2020

@author: Harry
"""

from types import MethodType
class Animal(object):

 def __init__(self, *args, **kwargs):
     self.name = kwargs.pop('name', None) or 'Animal'
     if kwargs.get('walk', None):
         self.walk = MethodType(kwargs.pop('walk'), self)
 def walk(self):
     message = '{} should implement a walk method'.format(self.__class__.__name__)
     raise NotImplementedError(message)
# Here are some different walking algorithms that can be used with Animal
def snake_walk(self):
 print('I am slithering side to side because I am a {}.'.format(self.name))
def four_legged_animal_walk(self):
 print('I am using all four of my legs to walk because I am a(n) {}.'.format(self.name))
def two_legged_animal_walk(self):
 print('I am standing up on my two legs to walk because I am a {}.'.format(self.name))
 
generic_animal = Animal()
king_cobra = Animal(name='King Cobra', walk=snake_walk)
elephant = Animal(name='Elephant', walk=four_legged_animal_walk)
kangaroo = Animal(name='Kangaroo', walk=two_legged_animal_walk)

kangaroo.walk()
elephant.walk()
king_cobra.walk()

# This one will Raise a NotImplementedError to let the programmer
# know that the walk method is intended to be used as a strategy.
generic_animal.walk()