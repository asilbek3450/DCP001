# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 02:14:03 2024

@author: Admin
"""

def all_even(numbers):
    return all(x % 2 == 0 for x in numbers)

if __name__ == "__main__":
    user_input = input("Enter a list of numbers (separated by spaces): ")
    numbers = list(map(int, user_input.split()))
    result = all_even(numbers)
    print(f"Are all numbers even? {result}")
