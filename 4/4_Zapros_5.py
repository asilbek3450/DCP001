# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 00:34:32 2024

@author: Admin
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка набора данных mtcars
mtcars = sns.load_dataset("mpg")

# Вывод первых строк данных
print(mtcars.head())

# Визуализация зависимости между мощностью (horsepower) и расходом топлива (mpg)
plt.figure(figsize=(8, 6))
sns.scatterplot(x="horsepower", y="mpg", data=mtcars, color="blue")
plt.title("Scatterplot of Horsepower vs. MPG")
plt.xlabel("Horsepower")
plt.ylabel("MPG")
plt.show()

# Вычисление коэффициента корреляции между мощностью и расходом топлива
correlation = mtcars["horsepower"].corr(mtcars["mpg"])
print(f"Correlation between Horsepower and MPG: {correlation:.2f}")

# Построение гистограммы распределения расхода топлива
plt.figure(figsize=(8, 6))
sns.histplot(mtcars["mpg"], bins=20, color="green", kde=True)
plt.title("Histogram of MPG")
plt.xlabel("MPG")
plt.show()
