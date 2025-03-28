# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 23:52:49 2024

@author: Admin
"""

from kanren import run, fact, var, Relation, lall

# Определение переменных
X, Y, Z = var(), var(), var()

# Определение отношений
parent = Relation()
ancestor = Relation()

# Добавление фактов
fact(parent, 'john', 'jim')
fact(parent, 'john', 'ann')
fact(parent, 'jim', 'mary')

# Правило: предок - это прямой родитель или родитель некоторого Z, который также является предком
def rule_ancestor(x, y):
    return lall((parent, x, y),) | lall((parent, x, Z), (ancestor, Z, y))

# Добавление правила в базу знаний
fact(ancestor, 'john', 'jim', True)
fact(ancestor, 'john', 'ann', True)
fact(ancestor, 'john', 'mary', True)

# Запрос: Кто является предком Джона?
result = run(1, Y, ancestor('john', Y, True))

# Вывод результата
if result:
    print(f"Предки Джона: {result}")
else:
    print("Нет предков Джона.")
