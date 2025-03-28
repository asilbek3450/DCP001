# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 02:38:06 2024

@author: Admin
"""

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def differentiate(self):
        # Производная многочлена
        return Polynomial([coef * i for i, coef in enumerate(self.coefficients[1:], start=1)])

    def __str__(self):
        # Представление многочлена в виде строки
        return " + ".join(f"{coef}x^{i}" if i > 0 else str(coef) for i, coef in enumerate(self.coefficients))

# Пример использования
if __name__ == "__main__":
    poly = Polynomial([3, -2, 0, 5])  # 3x^3 - 2x^2 + 0x + 5
    result = poly.differentiate()

    print(f"Исходный многочлен: {poly}")
    print(f"Производная: {result}")
