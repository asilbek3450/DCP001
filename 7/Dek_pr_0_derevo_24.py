# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 19:00:56 2023

@author: Admin
"""

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.key))
        if root.left or root.right:
            print_tree(root.left, level + 1, "L--- ")
            print_tree(root.right, level + 1, "R--- ")

# Создаем корень дерева
root = None
keys_to_insert = [5, 3, 7, 2, 4, 6, 8]

# Вставляем ключи в дерево
for key in keys_to_insert:
    root = insert(root, key)

# Выводим дерево
print_tree(root)
