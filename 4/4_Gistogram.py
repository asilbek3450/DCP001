# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 10:05:28 2024

@author: Admin
"""

import numpy as np
import matplotlib.pyplot as plt

# Генерация случайных данных
data = np.random.normal(loc=10, scale=2, size=100)

# Создание гистограммы
plt.hist(data, bins=20, color="lightblue", edgecolor="black")
plt.title("Histogram of Random Data")
plt.xlabel("Values")
plt.show()

# Вычисление среднего значения
mean_value = np.mean(data)
print(f"Mean Value: {mean_value}")
