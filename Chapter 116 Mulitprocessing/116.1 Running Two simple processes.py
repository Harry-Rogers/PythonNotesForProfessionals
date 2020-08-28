# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 13:09:55 2020

@author: Harry
"""

import multiprocessing
import time
from random import randint

def countUp():
    i = 0
    while i <=3:
        print('Up:\t{}'.format(i))
        time.sleep(randint(1,3)) # sleep for 1,2 or 3 secs
        i +=1
def countDown():
    i = 3
    while i>=0:
        print('Down:\t{}'.format(i))
        time.sleep(randint(1,3))
        i -=1
        
if __name__ == "__main__":
    workerUp = multiprocessing.Process(target=countUp())
    workerDown = multiprocessing.Process(target = countDown())
    
    workerUp.start()
    workerDown.start()
    
    workerUp.join()
    workerDown.join()