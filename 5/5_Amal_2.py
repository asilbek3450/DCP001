# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 01:22:53 2024

@author: Admin
"""

def fact(n):
    if n == 0:
        return 1
    elif n != 0:
        return n * fact(n - 1)

# Пример использования
print("The factorial of 4 is:")
print(fact(4))
