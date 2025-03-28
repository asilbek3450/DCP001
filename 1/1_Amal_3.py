# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 01:11:59 2024

@author: Admin
"""
def mother(person):
    mothers = {"дочь1": "Наташа", "дочь2": "Ольга", "дочь3": "Марина"}
    return person in mothers and mothers[person]

def women(person):
    daughters = ["дочь1", "дочь2", "дочь3"]
    return person in daughters

def age(person):
    ages = {"дочь1": 20, "дочь2": 25, "дочь3": 18}
    return ages.get(person, 0)

def full_age_daughter(mother, daughter, age):
    return mother(daughter) and women(daughter) and age(daughter) >= 18

# Пример использования
# Предположим, у вас есть функции mother, women и age

# Вызываем функцию
result = full_age_daughter(mother, "дочь1", age)

# Печатаем результат
print(result)



