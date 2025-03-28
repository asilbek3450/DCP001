# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 02:31:18 2024

@author: Admin
"""

def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    result = count_vowels(user_input)
    print(f"Number of vowels: {result}")
