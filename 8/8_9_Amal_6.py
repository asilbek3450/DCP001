# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 18:07:16 2024

@author: Admin
"""

# Определение класса Address
class Address:
    def __init__(self, city, street):
        self.city = city
        self.street = street

# Определение класса Person
class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

# Создание экземпляра структуры данных
john = Person("John", 25, Address("New York", "123 Main St"))

# Обновление данных
john.address.city = "John Doe"
john.age += 1

# Получение данных
city_name = john.address.city
print(f"City Name: {city_name}")
