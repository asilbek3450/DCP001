# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 13:49:26 2024

@author: Admin
"""

# Пример полиморфной функции в Python

# Обобщенная функция 'pair' принимает два аргумента любого типа и возвращает пару этих аргументов
def pair(x, y):
    return (x, y)

# Использование функции 'pair' с разными типами данных
result1 = pair(3.14, "Hello")
result2 = pair(True, False)

print(result1)
print(result2)
