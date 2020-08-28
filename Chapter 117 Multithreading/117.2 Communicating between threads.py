# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 12:42:48 2020

@author: Harry
"""

from queue import Queue
from threading import Thread

def producer(output_queue):
    while True:
        data = data_computation()
        
        output_queue.put(data)
        
def consumer(input_queue):
    while True:
        data = input_queue.get()
        
        input_queue.task_done()
def data_computation():
    return 0

q = Queue()
t1 = Thread(target=consumer(q))
t2 = Thread(target=producer(q))
t1.start()
t2.start()