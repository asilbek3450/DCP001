# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 10:45:49 2024

@author: Admin
"""

from kanren import run, eq, var, conde

bird = var()

def definitely_birds(bird):
    return conde([eq(bird, 'penguin')], [eq(bird, 'sparrow')])

def can_fly(bird):
    return eq(bird, 'sparrow')

sparrow_can_fly = run(1, bird, (definitely_birds, bird), (can_fly, bird))
print(f"Может ли воробей летать? {sparrow_can_fly[0] if sparrow_can_fly else 'неизвестно'}")

# Опционально, можно проверить, может ли пингвин летать
penguin_can_fly = run(1, bird, (definitely_birds, bird), (can_fly, bird))
print(f"Может ли пингвин летать? {penguin_can_fly[0] if penguin_can_fly else 'неизвестно'}")


