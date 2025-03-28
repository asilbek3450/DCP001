# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 02:39:31 2024

@author: Admin
"""

from itertools import count

def differentiate_polynomial(coefficients):
    # Дифференцирование многочлена
    return [coef * i for i, coef in enumerate(coefficients[1:], start=1)]

def format_polynomial(coefficients):
    # Представление многочлена в виде строки
    return " + ".join(f"{coef}x^{i}" if i > 0 else str(coef) for i, coef in enumerate(coefficients))

# Пример использования
if __name__ == "__main__":
    coefficients = [3, -2, 0, 5]  # Коэффициенты многочлена 3x^3 - 2x^2 + 0x + 5

    # Дифференцирование многочлена
    result_coefficients = differentiate_polynomial(coefficients)

    # Вывод результата
    print(f"Исходный многочлен: {format_polynomial(coefficients)}")
    print(f"Производная: {format_polynomial(result_coefficients)}")
