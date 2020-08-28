# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 14:49:54 2020

@author: Harry
"""

import threading

def foo():
    print("Hello threading!")

my_thread = threading.Thread(target=foo)
my_thread.start()
#cannot start again will cause runtime error 
    
# In cases where you split up one big job into several small ones and want to run them concurrently, but need to wait
# for all of them to finish before continuing, Thread.join() is the method you're looking for.
# For example, let's say you want to download several pages of a website and compile them into a single page. You'd
# do this:
    
import requests
from queue import Queue
from threading import Thread
q = Queue(maxsize=20)

def put_page_to_q(page_num):
    q.put(requests.get('http://some-website.com/page_%s.html' % page_num))
    
def compile(q):
    if not q.full():
        raise ValueError
    else:
        print("Done!")

threads = []
for page_num in range(20):
    t = Thread(target=requests.get, args=(page_num))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
    
compile(q)

# Using threading.Thread class we can subclass new custom Thread class. we must override run method in a
# subclass.

import time

class Sleepy(Thread):
    def run(self):
        time.sleep(5)
        print("Hello from thread!")
        
if __name__ == "__main__":
    t = Sleepy()
    t.start()
    t.join()
    print("The main program continues to run in the foreground")