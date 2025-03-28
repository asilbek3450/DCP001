# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 02:16:52 2024

@author: Admin
"""

def fibonacci(count):
    fib_list = [0, 1]
    while len(fib_list) < count:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return fib_list

if __name__ == "__main__":
    user_input = int(input("Enter the number of Fibonacci numbers to generate: "))
    result = fibonacci(user_input)
    print(f"Fibonacci sequence: {result}")
