# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 10:57:02 2024

@author: Admin
"""

# Импорт модуля для сортировки
from typing import List

# Функция сортировки списка
def sort_list(lst: List[int]) -> List[int]:
    return sorted(lst)

# Функция фильтрации четных чисел
def filter_even(lst: List[int]) -> List[int]:
    return list(filter(lambda x: x % 2 == 0, lst))

# Функция возведения в квадрат всех элементов списка
def square_list(lst: List[int]) -> List[int]:
    return list(map(lambda x: x**2, lst))

# Функция проверки принадлежности элемента к списку
def check_membership(lst: List[int], elem: int) -> bool:
    return elem in lst

def main():
    # Пример использования функций
    numbers = [5, 1, 3, 4, 2]
    print("Original List:", numbers)

    sorted_numbers = sort_list(numbers)
    print("Sorted List:", sorted_numbers)

    even_numbers = filter_even(numbers)
    print("Filtered List (even numbers):", even_numbers)

    squared_numbers = square_list(numbers)
    print("Squared List:", squared_numbers)

    # Проверка принадлежности элемента
    element_to_check = 3
    print(f"Is {element_to_check} in the list? {check_membership(numbers, element_to_check)}")

if __name__ == "__main__":
    main()
