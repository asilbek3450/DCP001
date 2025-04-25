# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 11:02:14 2024

@author: Admin
"""

def safe_divide(numerator, denominator):
    # Функция, возвращающая tuple в зависимости от условия
    if denominator == 0:
        return None
    else:
        return numerator // denominator

def main():
    print("Enter two numbers (numerator denominator):")
    input_str = input()
    numerator, denominator = map(int, input_str.split())

    # Получаем результат безопасного деления
    result = safe_divide(numerator, denominator)

    # Используем условие для вывода результата
    if result is not None:
        print(f"Result of division: {result}")
    else:
        print("Undefined (division by zero)")

if __name__ == "__main__":
    main()
