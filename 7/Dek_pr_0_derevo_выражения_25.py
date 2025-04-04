# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 23:57:44 2023

@author: Admin
"""

from kanren import run, eq, var, Relation, facts
import functools

# Определение отношения для бинарного дерева выражения
expr_tree_rel = Relation()

# Определение фактов о структуре выражения
facts(expr_tree_rel, ('+', '3', '4'), ('*', '2', '5'))

# Функция для вычисления значения выражения на основе дерева разбора
def evaluate_expression_tree(tree):
    operator, *operands = tree

    if operands:  # Если узел - оператор, рекурсивно вычисляем значения операндов
        operand_values = [evaluate_expression_tree(operand) for operand in operands]
        if operator == '+':
            return sum(operand_values)
        elif operator == '*':
            return 1 if not operand_values else functools.reduce(lambda x, y: x * y, operand_values)
    else:  # Если узел - операнд, возвращаем его значение
        return int(operator)

# Пример использования
expression_tree = ('+', ('*', '2', '5'), ('+', '3', '4'))

# Вычисляем значение выражения на основе дерева разбора
result = evaluate_expression_tree(expression_tree)

# Вывод результата
print("Значение выражения:", result)
