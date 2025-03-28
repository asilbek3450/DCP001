# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 02:27:35 2024

@author: Admin
"""

# Импорт модуля itertools
import itertools

# Функция для генерации итератора в арифметической прогрессии
def arithmetic_progression(a, d):
    current_value = a
    while True:
        yield current_value
        current_value += d

# Пример использования: генерация списка чисел, начиная с 1 с шагом 3
result_list = list(itertools.islice(arithmetic_progression(1, 3), 10))

# Вывод результата
print(result_list)

