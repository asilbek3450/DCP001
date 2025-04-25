# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 11:51:20 2024

@author: Admin
"""

from sympy import symbols, diff

# Определение переменной
x = symbols('x')

# Определение выражения
expression = x**2

# Дифференцирование
derivative = diff(expression, x)

# Вывод результата
print(derivative)
