# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 18:14:14 2024

@author: Admin
"""

from kanren import run, eq, var

# Определение переменных
X = var()

# Фактические свойства объекта Z
facts_list = (
    (eq, 'Z', 'red'),
)

# Правило: Объект X обладает свойствами "красный" и "круглый".
def has_property_rule(x):
    return (eq, x, 'red'), (eq, x, 'round')

# Правило: Модальность "необходимо" (must)
def must_be_rule(x, property_set):
    return has_property_rule(x) if property_set == 'red_and_round' else False

# Правило: Модальность "возможно" (may)
def may_be_rule(x, property_set):
    return has_property_rule(x) if property_set == 'red_and_round' else False

# Добавление фактов
for fact in facts_list:
    run(1, fact)

# Запрос: Объект X фактически является красным и круглым?
actual_result = run(1, X, *has_property_rule(X))
if actual_result:
    print(f"Объект {actual_result[0]} фактически является красным и круглым.")
else:
    print("Фактически объект не является красным и круглым.")

# Запрос: Объект X должен быть красным и круглым?
must_be_result = run(1, X, *must_be_rule(X, 'red_and_round'))
if must_be_result:
    print(f"Объект {must_be_result[0]} должен быть красным и круглым.")
else:
    print("Необходимо, чтобы объект был красным и круглым.")

# Запрос: Объект X может быть красным и круглым?
may_be_result = run(1, X, *may_be_rule(X, 'red_and_round'))
if may_be_result:
    print(f"Объект {may_be_result[0]} может быть красным и круглым.")
else:
    print("Возможно, что объект может быть красным и круглым.")
