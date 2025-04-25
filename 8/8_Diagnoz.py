# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 13:22:39 2024

@author: Admin
"""

from kanren import run, eq, membero, conde, var, Relation, facts, lall

# Определение симптомов и правил диагноза
symptom = Relation()
facts(symptom, "cough")
facts(symptom, "fever")
facts(symptom, "feeling_weak")

diagnosis = var()

# Правила диагноза
rules = conde(
    (eq(symptom, "cough"), eq(symptom, "fever"), eq(diagnosis, "cold")),
    (eq(symptom, "cough"), eq(symptom, "fever"), eq(symptom, "feeling_weak"), eq(diagnosis, "flu")),
    (eq(symptom, "feeling_weak"), conde((eq(symptom, "cough"), False), (eq(symptom, "fever"), False)), eq(diagnosis, "fatigue"))
)

# Пользовательский вопрос
def ask_user():
    for s in ["cough", "fever", "feeling_weak"]:
        response = input(f"Do you have {s}? (yes/no): ").lower()
        if response == "yes":
            facts(symptom, s)

# Диагностика на основе введенных симптомов
def diagnose():
    result = run(0, diagnosis, rules)
    
    if result:
        print("You may have", result[0] + ".")
    else:
        print("Unable to diagnose based on provided symptoms.")

# Запуск программы
ask_user()
diagnose()
