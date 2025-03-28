# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 23:52:04 2024

@author: Admin
"""

def list_length(lst):
    if not lst:
        return 0
    else:
        return 1 + list_length(lst[1:])

# Примеры использования
print(list_length([123446, 232, 2332, 23]))  # Вывод: 4
print(list_length([123446, 232, 2332, 23, 'sdfds', 'sdfsf', 'sdfa', 'asd']))  # Вывод: 8
print(list_length([]))  # Вывод: 0
print(list_length([1]))  # Вывод: 1
print(list_length([1, 9, 8, 7, 6, 5, 4, 3, 2]))  # Вывод: 9
