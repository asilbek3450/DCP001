123456# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 02:36:20 2024

@author: Admin
"""

def is_palindrome(sequence):
    return sequence == sequence[::-1]

if __name__ == "__main__":
    user_input = input("Enter a sequence (e.g., a string or list of numbers): ")
    result = "Palindrome" if is_palindrome(user_input) else "Not a palindrome"
    print(result)
