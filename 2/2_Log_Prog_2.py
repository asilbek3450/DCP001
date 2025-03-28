# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 21:55:18 2024

@author: Admin
"""

from kanren import run, eq, facts, var

# Определение переменных
X = var()

# Определение фактов
facts_list = (
    (eq, 'cat', 'animal'),
    (eq, 'dog', 'animal')
)

# Добавление фактов
for fact in facts_list:
    run(1, fact)

# Определение правила
def has_four_legs(x):
    return run(1, x, eq(x, 'cat'))

# Запрос: Может ли кошка двигаться?
result = has_four_legs(X)

# Вывод результата
if result:
    print("Кошка может двигаться.")
else:
    print("Кошка не может двигаться.")
