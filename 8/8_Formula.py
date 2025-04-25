# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 10:31:23 2024

@author: Admin
"""

from sympy import symbols, simplify, Eq, solve

# Определение переменных
X = symbols('X')

# Правило: упрощение атомарного выражения
def simplify_atomic(expr):
    return expr

# Правило: упрощение выражения X + 0
def simplify_plus_zero(expr):
    return simplify(expr)

# Правило: упрощение выражения X * 1
def simplify_times_one(expr):
    return simplify(expr)

# Пример использования
if __name__ == "__main__":
    # Примеры выражений
    expression1 = X
    expression2 = X + 7+2*X
    
    
    expression3 = X * 1

    # Применение правил упрощения
    simplified_expression1 = simplify_atomic(expression1)
    simplified_expression2 = simplify_plus_zero(expression2)
    simplified_expression3 = simplify_times_one(expression3)

    # Вывод результатов
    print(f"Simplified expression 1: {simplified_expression1}")
    print(f"Simplified expression 2: {simplified_expression2}")
    print(f"Simplified expression 3: {simplified_expression3}")
