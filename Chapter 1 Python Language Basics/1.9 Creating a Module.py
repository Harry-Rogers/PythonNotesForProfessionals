# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 14:40:42 2020

@author: Harry
"""
import hello
#hello module has one function that is say_hello that prints hello!
hello.say_hello()
#module then function

from hello import say_hello
say_hello()
#can import just one function 

from hello import say_hello as go
go()
#Can alias modules as variable names

if __name__ == '__main__':
    from hello import say_hello
    say_hello()
#can create stand alone runnable script