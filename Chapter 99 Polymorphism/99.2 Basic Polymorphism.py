# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 12:41:56 2020

@author: Harry
"""
class Shape:
    def calculate_area(self):
        return 0
class Square(Shape):
    side_length = 2
    def calculate_area(self):
        return self.side_length *2
class Triangle(Shape):
    base_length = 4
    height = 3
    def calculate_area(self):
        return 0.5 * self.base_length * self.height

def get_area(input_obj):
    print(input_obj.calculate_area())

# Objects
shape_obj = Shape()
square_obj = Square()
triangle_obj = Triangle()
# Get area of objects
get_area(shape_obj)
get_area(square_obj)
get_area(triangle_obj)