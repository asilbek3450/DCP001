# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 22:42:33 2023

@author: Admin
"""

from kanren import run, eq, membero, var

# Создаем переменные
x, y, z = var(), var(), var()

# Определяем отношение для списка
list_relation = (eq, x, (1, (2, (3, (4, (5, (6, (7,))))))))

# Используем membero для поиска элемента в списке
query_result = run(1, x, membero(3, list_relation))
print("Элемент 3 найден в списке:", query_result)
