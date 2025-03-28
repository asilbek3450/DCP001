# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 10:01:55 2024

@author: Admin
"""

# Определение функции factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Пример использования
result = factorial(5)  # Вычисление факториала числа 5

# Вывод результата
print(result)
