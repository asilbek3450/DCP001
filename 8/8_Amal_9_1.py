# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 12:08:33 2024

@author: Admin
"""

class Just:
    def __init__(self, value):
        self.value = value

    def bind(self, func):
        return func(self.value)

    def map(self, func):
        return Just(func(self.value))

    def get_or_else(self, default):
        return self.value

    def is_some(self):
        return True

    def get(self):
        return self.value


def create_just(value):
    return Just(value)


def maybe_example():
    # Пример использования "монады" Maybe
    maybe_result = (
        create_just(5)
        .bind(lambda x: create_just(3).bind(lambda y: create_just(2).map(lambda z: x * y * z)))
        .get_or_else(None)
    )

    print(f"Maybe monad result: {maybe_result}")


if __name__ == "__main__":
    maybe_example()
