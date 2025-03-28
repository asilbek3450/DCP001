# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 18:00:40 2024

@author: Admin
"""

from kanren import run, eq, var

# Определение переменных
X = var()

# Определение фактов
facts = (
    ('Человек', 'Человек'),
    ('Человек', 'Сократ')
)

# Определение правила
def mortal_rule(x):
    return run(1, x, eq(x, 'Сократ'))

# Добавление фактов
for fact in facts:
    run(1, fact)

# Запрос: Сократ смертен?
result = mortal_rule(X)

# Вывод результата
if result:
    print(f"{result[0]} смертен.")
else:
    print(f"{result[0]} бессмертен.")
