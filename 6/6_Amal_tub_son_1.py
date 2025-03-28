# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 02:28:43 2024

@author: Admin
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    user_input = int(input("Enter a number: "))
    result = "Prime" if is_prime(user_input) else "Not prime"
    print(result)
