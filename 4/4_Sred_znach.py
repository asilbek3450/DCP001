# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 10:11:56 2024

@author: Admin
"""

# Функция для вычисления среднего значения списка чисел
def average(numbers):
    return sum(numbers) / len(numbers) if len(numbers) > 0 else 0

# Пример использования
if __name__ == "__main__":
    numeric_list = [1.0, 2.5, 3.0, 4.5, 5.0]
    print("Original List:", numeric_list)
    print("Average:", average(numeric_list))
