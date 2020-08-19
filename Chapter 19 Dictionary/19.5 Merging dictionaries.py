# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 16:15:45 2020

@author: Harry
"""

fish = {'name': "Nemo", 'hands': "fins", 'special': "gills"}
dog = {'name': "Clifford", 'hands': "paws", 'color': "red"}
fishdog = {**fish, **dog}
print(fishdog)
dogfish = {**dog, **fish}
print(dogfish)
