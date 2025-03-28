# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 00:24:48 2024

@author: Admin
"""

from itertools import permutations

def einstein_puzzle():
    nationalities = ["Brit", "Swede", "Dane", "German", "Norwegian"]
    colors = ["Red", "Green", "Yellow", "Blue", "White"]
    drinks = ["Tea", "Coffee", "Milk", "Beer", "Water"]
    cigarettes = ["Blend", "Blue Master", "Dunhill", "Pall Mall", "Prince"]
    pets = ["Dogs", "Cats", "Birds", "Horses", "Fish"]

    # Генерация всех возможных перестановок для каждой категории
    permutations_list = list(permutations(nationalities))
    for p in permutations_list:
        for c in permutations(colors):
            for d in permutations(drinks):
                for s in permutations(cigarettes):
                    for pet in permutations(pets):
                        # Дополнительные условия для уменьшения перебора
                        if "Norwegian" not in p or "Blue" not in c:
                            continue
                        if "Blend" not in s or "Cats" not in pet:
                            continue
                        if "Dunhill" not in s or "Horses" not in pet:
                            continue
                        if "German" not in p or "Prince" not in s:
                            continue

                        # Проверка условий
                        if c.index("Green") == c.index("White") - 1 and \
                           s.index("Blend") == pet.index("Cats") - 1 and \
                           s.index("Blue Master") == d.index("Beer") and \
                           p.index("Norwegian") == c.index("Blue") - 1 and \
                           p.index("Norwegian") == d.index("Water") - 1 and \
                           p.index("Brit") == c.index("Red") and \
                           p.index("Swede") == pet.index("Dogs") and \
                           s.index("Dunhill") == pet.index("Horses") and \
                           s.index("Pall Mall") == pet.index("Birds") and \
                           p.index("German") == s.index("Prince") and \
                           c.index("Yellow") == d.index("Milk") - 1 and \
                           s.index("Blend") == d.index("Water") - 1:
                            # Вывод результата
                            result = list(zip(p, c, d, s, pet))
                            return result

print("Решение головоломки Эйнштейна:")
solution = einstein_puzzle()
for item in solution:
    print(item)

