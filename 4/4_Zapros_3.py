# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 00:08:05 2024

@author: Admin
"""

from kanren import run, fact, var, Relation, lall

# Определение переменных
X = var()

# Определение отношений
enrolled = Relation()
successful_student = Relation()

# Добавление фактов
fact(enrolled, 'john', 'math')
fact(enrolled, 'john', 'physics')
fact(enrolled, 'mary', 'math')
fact(enrolled, 'bob', 'physics')
fact(enrolled, 'bob', 'english')

# Правило: успешный студент - тот, кто посещает курс "Математика"
def rule_successful_student(x):
    return lall((enrolled, x, 'math'))

# Запросы
result_john = run(1, X, rule_successful_student(X))

# Вывод результатов
print(f"Для Джона успешен: {bool(result_john)}")
