# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 02:29:36 2024

@author: Admin
"""

# Функция для генерации списка в арифметической прогрессии
def arithmetic_progression(a, d, n):
    return [a + i * d for i in range(n)]

# Пример использования: генерация списка чисел, начиная с 1 с шагом 3
result_list = arithmetic_progression(1, 3, 10)

# Вывод результата
print(result_list)
