# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 13:55:53 2024

@author: Admin
"""

from abc import ABC, abstractmethod
from math import pi

# Абстрактный базовый класс Shape с методом area
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Класс Circle, унаследованный от Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius * self.radius

# Класс Square, унаследованный от Shape
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

# Пример использования полиморфизма
def main():
    # Полиморфное использование - список фигур любого типа
    shapes = [Circle(5.0), Square(4.0)]

    # Вызов метода area() для каждой фигуры, не зная их конкретных типов
    for shape in shapes:
        print(f"Площадь фигуры: {shape.area()}")

if __name__ == "__main__":
    main()
