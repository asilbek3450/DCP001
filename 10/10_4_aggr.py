# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 23:19:27 2023

@author: Admin
"""

import pandas as pd

# Создадим DataFrame с данными о клиентах и их возрастом
клиенты = pd.DataFrame({
    'имя': ['Анна', 'Иван', 'Мария', 'Петр'],
    'возраст': [25, 30, 22, 28]
})

# Вычислим средний возраст всех клиентов
средний_возраст = клиенты['возраст'].mean()

# Вывод результатов
print(f"Средний возраст всех клиентов: {средний_возраст}")
