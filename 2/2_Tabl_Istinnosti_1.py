# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 18:39:47 2024

@author: Admin
"""

def truth_value(P, Q):
    result = P & Q
    return result

# Пример использования
result = truth_value(1, 0)
print(f'Result = {result}')