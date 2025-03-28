# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 15:44:34 2024

@author: Admin
"""

from kanren import Relation, facts, run, conde, var

# Определение отношения (факты)
parent = Relation()
facts(parent, ("John", "Jim"), ("John", "Bob"), ("Bob", "Alice"))

# Создание переменных
x, y = var(), var()

# Запрос на отношение "родитель"
query_result = run(0, x, parent(x, y))
print("Все отношения 'родитель':", query_result)

# Определение правила (дедушка)
grandparent = Relation()
rules = conde((parent(x, y), parent(y, x), grandparent(x, y)))

# Добавление правила в базу знаний
facts(grandparent, ("John", "Alice"))

# Запрос на отношение "дедушка"
query_result = run(0, x, grandparent(x, "Alice"))
print("Все отношения 'дедушка':", query_result)
