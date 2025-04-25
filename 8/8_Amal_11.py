# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 14:11:40 2024

@author: Admin
"""

import sys

def command_line_arguments():
    args = sys.argv[1:]  # Исключаем имя исполняемого файла из списка аргументов
    print("Command line arguments:", args)

if __name__ == "__main__":
    command_line_arguments()


import sys

def executable_name():
    executable = sys.executable
    print("Executable name:", executable)

if __name__ == "__main__":
    executable_name()
    
import os

def environment_variable():
    home_dir = os.environ.get("HOMEPATH")  # Изменено на HOMEPATH
    print("Home directory:", home_dir)

if __name__ == "__main__":
    environment_variable()



import os

def environment_operations():
    os.putenv("MY_VARIABLE", "some_value")
    my_variable = os.environ.get("MY_VARIABLE")
    print("My variable:", my_variable)

    os.unsetenv("MY_VARIABLE")  # Изменено на unsetenv
    # Теперь переменной MY_VARIABLE не существует



if __name__ == "__main__":
    environment_operations()
