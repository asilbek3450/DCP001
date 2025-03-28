# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 23:58:02 2024

@author: Admin
"""

from kanren import run, fact, var, Relation, lall

# Определение переменных
X, Y, Z = var(), var(), var()

# Определение отношений
parent = Relation()
brother = Relation()

# Добавление фактов
fact(parent, 'john', 'jim')
fact(parent, 'john', 'ann')
fact(parent, 'jim', 'mary')
fact(parent, 'jim', 'bob')

# Правило: определение отношения "брат"
def rule_brother(x, y):
    return lall((parent, z, x), (parent, z, y), (x != y,))

# Добавление правила в базу знаний
fact(brother, 'bob', 'mary', True)

# Запрос: Кто является братом Мэри?
result_mary = run(1, X, brother(X, 'mary', True))

# Вывод результата для Мэри
if result_mary:
    print(f"Брат Мэри: {result_mary[0]}")
else:
    print("Нет брата Мэри.")

# Запрос: Кто является братом Джима?
result_jim = run(1, X, brother(X, 'jim', True))

# Вывод результата для Джима
if result_jim:
    print(f"Брат Джима: {result_jim[0]}")
else:
    print("Нет брата Джима.")
