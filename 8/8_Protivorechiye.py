# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 12:13:04 2024

@author: Admin
"""

from kanren import run, eq, var, conde, facts

# Определение утверждений
definitely_birds = conde((eq('penguin', 'bird'),), (eq('sparrow', 'bird'),), (eq('eagle', 'bird'),))
can_fly = conde((eq('sparrow', 'can_fly'),), (eq('penguin', 'cannot_fly'),), (eq('eagle', 'can_fly'),))

# Факты для использования в запросах
facts(definitely_birds[0])
facts(can_fly[0])

# Проверка противоречий в системе утверждений
def check_consistency():
    statements = run(0, var(), definitely_birds)
    for statement in statements:
        result = run(0, var(), can_fly[0])
        if not result:
            print(f"Противоречие: {statement}")
            return False  # Прекратить выполнение функции, если есть противоречие
    print("Система утверждений согласована.")
    return True  # Вернуть True, если противоречий не найдено

# Вызов функции для проверки противоречий
check_consistency()
