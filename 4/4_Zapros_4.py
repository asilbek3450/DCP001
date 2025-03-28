# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 00:28:21 2024

@author: Admin
"""

def sublist(xs, ys):
    if not xs:
        return True
    if xs == ys[:len(xs)]:
        return True
    return sublist(xs, ys[1:])

# Пример использования
if sublist([2, 3], [1, 2, 3, 4]):
    print("The list [2, 3] is a sublist of [1, 2, 3, 4]")
else:
    print("The list [2, 3] is not a sublist of [1, 2, 3, 4]")
