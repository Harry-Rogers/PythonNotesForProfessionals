# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 15:27:00 2020

@author: Harry
"""
import datetime
aDate = None
print(aDate)
#if aDate is None:
    #aDate = datetime.date.today()
    #print(aDate)

#optimised test below as this will eval with not and none to true
if not aDate:
    aDate = datetime.date.today()
    print(aDate)