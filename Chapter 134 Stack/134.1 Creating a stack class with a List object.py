# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 14:40:36 2020

@author: Harry
"""

#define a stack class
class Stack:
    
    def __init__(self):
        self.items = []

 #method to check the stack is empty or not
    def isEmpty(self):
        return self.items == []

 #method for pushing an item
    def push(self, item):
        self.items.append(item)
 #method for popping an item
    def pop(self):
        return self.items.pop()

 #check what item is on top of the stack without removing it
    def peek(self):
        return self.items[-1]
 #method to get the size
    def size(self):
        return len(self.items)
 #to view the entire stack
    def fullStack(self):
        return self.items
    
stack = Stack()
print('Current stack:', stack.fullStack())
print('Stack empty?:', stack.isEmpty())
print('Pushing integer 1')
stack.push(1)
print('Pushing string "Told you, I am generic stack!"')
stack.push('Told you, I am generic stack!')
print('Pushing integer 3')
stack.push(3)
print('Current stack:', stack.fullStack())
print('Popped item:', stack.pop())
print('Current stack:', stack.fullStack())
print('Stack empty?:', stack.isEmpty())