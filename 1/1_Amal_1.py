# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 23:46:50 2024

@author: Admin
"""

# Пример данных (замените этот список своими значениями)
column_values = [5, 8, 3, 12, 7, 2, 10, 6, 15, 4]

# Инициализация переменной минимального значения
min_value = column_values[0]

# Поиск минимального значения
for value in column_values:
    if value < min_value:
        min_value = value

# Вывод минимального значения
print("Минимальное значение:", min_value)





def find_min(lst, min_val=None):
    if not lst:
        return min_val
    else:
        head, *tail = lst
        new_min = head if min_val is None or head < min_val else min_val
        return find_min(tail, new_min)

# Пример данных (замените этот список своими значениями)
my_list = [5, 8, 3, 12, 7, 2, 10, 6, 15, 4]

# Вызов функции
result = find_min(my_list)

# Вывод минимального значения
print("Минимальное значение:", result)
