# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 17:54:18 2024

@author: Admin
"""

import numpy as np

# Создание массива
my_array = np.array([1, 2, 3, 4, 5])

# Изменение элемента массива
my_array[2] = 10
print(my_array)

# Получение элемента по индексу
element_at_index = my_array[2]
print(element_at_index)

# Преобразование массива
doubled_array = my_array * 2
print(doubled_array)
