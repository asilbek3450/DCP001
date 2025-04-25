# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 12:05:11 2024

@author: Admin
"""

def maybe_example():
    # Пример использования "монады" Maybe
    maybe_result = (
        Some(5)
        .bind(lambda x: Some(3).bind(lambda y: Some(2).map(lambda z: x * y * z)))
        .get_or_else(None)
    )

    print(f"Maybe monad result: {maybe_result}")


def io_example():
    # Пример использования "монады" IO (ввода-вывода)
    print("Enter two numbers:")
    input1 = input()
    input2 = input()

    maybe_sum = (
        read_maybe(input1)
        .bind(lambda num1: read_maybe(input2).map(lambda num2: num1 + num2))
    )

    if maybe_sum.is_some():
        print(f"Sum: {maybe_sum.get()}")
    else:
        print("Invalid input. Please enter numbers.")


# Вспомогательный класс для представления Maybe
class Maybe:
    def __init__(self, value):
        self.value = value

    def bind(self, func):
        if self.value is not None:
            return func(self.value)
        else:
            return Maybe(None)

    def map(self, func):
        return Maybe(func(self.value)) if self.value is not None else Maybe(None)

    def get_or_else(self, default):
        return self.value if self.value is not None else default

    def is_some(self):
        return self.value is not None

    def get(self):
        return self.value


# Вспомогательная функция для безопасного чтения чисел
def read_maybe(s):
    try:
        return Maybe(int(s))
    except ValueError:
        return Maybe(None)


if __name__ == "__main__":
    maybe_example()
    io_example()
