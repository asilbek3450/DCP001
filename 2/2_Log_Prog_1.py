# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 19:32:20 2024

@author: Admin
"""

from kanren import run, eq, var

# Определение переменных
X = var()

# Определение фактов о животных
facts_list = (
    (eq, 'cat', 'animal'),
    (eq, 'dog', 'animal')
)

# Определение правила о том, что все животные с четырьмя ногами
def has_four_legs(x):
    return run(1, x, eq(x, 'cat'))

# Добавление фактов
for fact in facts_list:
    run(1, fact)

# Запрос: Есть ли у кошки четыре ноги?
result = has_four_legs(X)

# Вывод результата
if result:
    print(f"{result[0]} имеет четыре ноги.")
else:
    print("Объект не найден или у него не четыре ноги.")
