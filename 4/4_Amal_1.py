# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 00:45:37 2024

@author: Admin
"""

from math import pi

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return pi * self.radius**2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Пример использования
circle_example = Circle(5.0)
rectangle_example = Rectangle(4.0, 6.0)

print("Площадь круга:", circle_example.area())
print("Площадь прямоугольника:", rectangle_example.area())
