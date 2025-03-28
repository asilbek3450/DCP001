# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 02:08:55 2024

@author: Admin
"""

def st(x, y):
    if y == 1:
        return x
    elif y > 1:
        return st(x, y - 1) * x

# Пример использования
result = st(2, 3)
print(result)




def st(x, y):
    if y == 1:
        return x
    else:
        yy = y - 1
        zz = st(x, yy)
        return zz * x

# Пример использования
result = st(3, 4)
print(result)
