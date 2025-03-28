# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 18:44:17 2024

@author: Admin
"""

def truth_table():
    header = ["P", "Q", "P AND Q"]
    print("|".join(header))

    for P in [0, 1]:
        for Q in [0, 1]:
            result = P & Q
            row = [str(P), str(Q), str(result)]
            print("|".join(row))

# Вызов функции для создания таблицы истинности
truth_table()
