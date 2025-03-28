# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 01:04:27 2024

@author: Admin
"""

def add(x, y):
    if x == 0:
        return y
    elif y == 0:
        return x
    else:
        return x + y

# Пример использования сопоставления с образцом
print("The addition of the two numbers is:")
print(add(2, 5))
