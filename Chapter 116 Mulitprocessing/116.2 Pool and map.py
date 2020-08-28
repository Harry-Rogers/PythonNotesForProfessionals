# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 14:46:51 2020

@author: Harry
"""

from multiprocessing import Pool

def cube(x):
 return print(x ** 3)

if __name__ == "__main__":
    pool = Pool(1)
    result = pool.map(cube, [0, 1, 2, 3])
    print(result)
 #major pc lag no prints either