# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 09:42:45 2024

@author: Admin
"""

def all_positive(lst):
    return all(x > 0 for x in lst)

# Запрос
result = all_positive([1, 2, 3])

# Вывод результата
print(result)
