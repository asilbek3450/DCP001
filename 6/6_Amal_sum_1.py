# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 01:55:42 2024

@author: Admin
"""

def sum_up_to(n):
    return sum(range(1, n + 1))

if __name__ == "__main__":
    user_input = int(input("Enter a number: "))
    result = sum_up_to(user_input)
    print(f"Sum of numbers up to {user_input} is: {result}")
