# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 10:42:08 2024

@author: Admin
"""

# Пример работы с целыми числами и списками
def main():
    print("Hello, Python!")

    # Определение списка целых чисел
    numbers = [1, 2, 3, 4, 5]

    # Использование базовых функций для работы со списком
    print("Original List:", numbers)
    print("Length of List:", len(numbers))
    print("Sum of List:", sum(numbers))

    # Применение лямбда-выражения к каждому элементу списка
    squared_numbers = list(map(lambda x: x**2, numbers))
    print("Squared List:", squared_numbers)

    # Использование булевых операций
    is_even = lambda x: x % 2 == 0
    print("Are all numbers even?", all(is_even(x) for x in numbers))

    # Работа с кортежами
    tuple_example = (1, "Python", True)
    print("Tuple Example:", tuple_example)

if __name__ == "__main__":
    main()
