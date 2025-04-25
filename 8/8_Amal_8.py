# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 11:26:13 2024

@author: Admin
"""

def file_handling_operations():
    # Открытие файла в режиме для чтения
    with open("example.txt", "r") as file:
        # Чтение из файла
        content = file.read()
        print(content)

# Вызов функции
file_handling_operations()
