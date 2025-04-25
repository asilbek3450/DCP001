# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 17:41:26 2024

@author: Admin
"""

my_dict = {"apple": 3, "banana": 2, "orange": 5}

# Добавление новой пары ключ-значение
my_dict["grape"] = 4

# Поиск значения по ключу
print(my_dict.get("banana", "Key not found"))
