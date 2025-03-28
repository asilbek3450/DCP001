# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 23:16:10 2024

@author: Admin
"""

from kanren import run, conde, var, eq

# Определение отношений
def study(who, what):
    return conde((eq(who, 'mark'), eq(what, 'book')),
                 (eq(who, 'mark'), eq(what, 'studentbook')),
                 (eq(who, 'mark'), eq(what, 'docs')),
                 (eq(who, 'masha'), eq(what, 'mouse')),
                 (eq(who, 'masha'), eq(what, 'book')),
                 (eq(who, 'masha'), eq(what, 'notebook')),
                 (eq(who, 'masha'), eq(what, 'mark')),
                 (eq(who, 'misha'), eq(what, 'math')),
                 (eq(who, 'misha'), eq(what, 'lp')),
                 (eq(who, 'misha'), eq(what, 'docs')),
                 (eq(who, 'misha'), eq(what, 'studentbook')))

# Определение переменных
who = var()

# Запрос: Кто изучал документацию?
result = run(1, who, study(who, 'docs'))
print(f"Кто изучал документацию? {result[0]}")

# Запрос: Кто и что изучал?
result = run(1, (who, var()), study(who, var()))
print("Кто и что изучал?")
for item in result:
    print(f"{item[0]} изучал {item[1]}")
