# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 23:29:37 2024

@author: Admin
"""

class Person:
    def __init__(self, name):
        self.name = name

facts = [
    ("Sasha", "Lesha"),
    ("Misha", "Sasha"),
    ("Misha", "Dasha"),
    ("Masha", "Misha"),
]

def is_older(person1, person2):
    for fact in facts:
        if fact[0] == person1.name and fact[1] == person2.name:
            return True
    return False

def is_older_recursive(person1, person2):
    for fact in facts:
        if fact[0] == person1.name and fact[1] == person2.name:
            return True
        elif fact[0] == person1.name:
            next_person = Person(fact[1])
            return is_older_recursive(next_person, person2)
    return False

# Примеры использования
sasha = Person("Sasha")
lesha = Person("Lesha")
misha = Person("Misha")
dasha = Person("Dasha")
masha = Person("Masha")

print(is_older(sasha, lesha))  # Саша старше Лёши
print(is_older_recursive(masha, lesha))  # Маша старше Лёши через свои правила
