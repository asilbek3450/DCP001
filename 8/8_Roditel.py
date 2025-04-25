# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 10:27:20 2024

@author: Admin
"""

class Person:
    def __init__(self, name):
        self.name = name

# Факты о родителях
john = Person("John")
jane = Person("Jane")
jim = Person("Jim")

# Определение отношения "родитель"
def father(x, y):
    return (x, y) in [(john, jim)]

def mother(x, y):
    return (x, y) in [(jane, jim)]

# Определение отношения "родитель" с использованием "или"
def parent(x, y):
    return father(x, y) or mother(x, y)

# Пример использования
if __name__ == "__main__":
    print(f"Is John a father of Jim? {father(john, jim)}")
    print(f"Is Jane a mother of Jim? {mother(jane, jim)}")
    print(f"Is John/Jane a parent of Jim? {parent(john, jim) or parent(jane, jim)}")
