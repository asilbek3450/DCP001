# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 19:53:32 2023

@author: Admin
"""

from kanren import run, eq, var, Relation, facts

# Определяем отношение для бинарного дерева
binary_tree_rel = Relation()

# Добавляем факты о дереве
#facts(binary_tree_rel, ('A', 'B', 'C'), ('B', 'D', 'E'), ('C', None, 'F'), ('D', None, None), ('E', None, None), ('F', None, None))
facts(binary_tree_rel, ('+', '3', '4'), ('*', '2', '5'))
# Переменные для представления дерева и его компонентов
tree_var, left_branch_var, right_branch_var = var(), var(), var()

# Поиск корня дерева
root_result = run(1, tree_var, binary_tree_rel(tree_var, left_branch_var, right_branch_var))

# Вывод результатов
if root_result:
    print("Корень дерева:", root_result[0])

# Поиск левой ветви корня
left_branch_result = run(1, left_branch_var, binary_tree_rel(root_result[0], left_branch_var, var()))
if left_branch_result:
    print("Левая ветвь корня:", left_branch_result[0])

# Поиск правой ветви корня
right_branch_result = run(1, right_branch_var, binary_tree_rel(root_result[0], var(), right_branch_var))
if right_branch_result:
    print("Правая ветвь корня:", right_branch_result[0])
