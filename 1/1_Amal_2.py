# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 00:45:04 2024

@author: Admin
"""

numbers = [1, 2, 3, 4, 5]
total = 0
for num in numbers:
    total += num
print(total)


numbers = [1, 2, 3, 4, 5]
total = sum(numbers)
print(total)

class Calculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_total(self):
        return sum(self.numbers)

numbers = [1, 2, 3, 4, 5]
calc = Calculator(numbers)
total = calc.calculate_total()
print(total)

numbers = [1, 2, 3, 4, 5]
total = sum(map(lambda x: x * 2, numbers))
print(total)
