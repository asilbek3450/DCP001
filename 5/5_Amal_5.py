# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 01:42:51 2024

@author: Admin
"""

# Пример использования лямбда-выражения и функции map
numbers = [1, 2, 3, 4, 5]
print("Original list:")
print(numbers)

doubled_numbers = list(map(lambda x: x * 2, numbers))
print("List after doubling each element:")
print(doubled_numbers)
