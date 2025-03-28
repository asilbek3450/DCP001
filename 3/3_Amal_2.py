# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 22:57:19 2024

@author: Admin
"""

from kanren import Relation, facts, run, conde, var

# Определение отношений (фактов)
study = Relation()
see = Relation()

# Добавление фактов в базу знаний
facts(study, ('mark', 'book'))
facts(study, ('mark', 'studentbook'))
#facts(study, ('mark', 'docs'))

facts(see, ('masha', 'mouse'))
facts(see, ('masha', 'book'))
facts(see, ('masha', 'notebook'))
facts(see, ('masha', 'mark'))

facts(study, ('misha', 'math'))
facts(study, ('misha', 'lp'))
facts(study, ('misha', 'docs'))
facts(study, ('misha', 'studentbook'))

# Запросы
x = var()

# Запрос: "Марк изучает книгу?"
result = run(1, x, study('mark', 'book'))
print("Марк изучает книгу." if result else "Марк не изучает книгу.")

# Запрос: "Марк изучает документацию?"
result = run(1, x, study('mark', 'docs'))
print("Марк изучает документацию." if result else "Марк не изучает документацию.")
