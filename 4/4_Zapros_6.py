# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 00:41:31 2024

@author: Admin
"""

def sum_of_even_squares(numbers):
    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    squares = map(lambda x: x**2, even_numbers)
    return sum(squares)

# Пример использования
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Original List:", numbers)
    print("Sum of Squares of Even Numbers:", sum_of_even_squares(numbers))
