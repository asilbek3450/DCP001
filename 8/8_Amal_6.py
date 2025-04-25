# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 11:24:07 2024

@author: Admin
"""

def file_operations():
    # Запись в файл
    with open("example.txt", "w") as file:
        file.write("Hello, Haskell!")

    # Чтение из файла
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)

if __name__ == "__main__":
    file_operations()
