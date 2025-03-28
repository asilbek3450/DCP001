# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 22:53:27 2024

@author: Admin
"""

from kanren import run, eq, membero, var, facts

# Определение переменных
x = var()

# Утверждение факта "Марк не изучает книгу"
facts((('study', 'mark', 'book'),))

# Запрос: "Марк не изучает книгу"
result = run(0, x, eq(x, ('study', 'mark', 'book')))
print("Марк не изучает книгу." if not result else "Марк изучает книгу.")
