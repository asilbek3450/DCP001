# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 00:48:54 2024

@author: Admin
"""

class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

# Функция для вычисления суммарной стоимости товаров в корзине
def total_cost(products):
    return sum(product.price for product in products)

# Пример использования
if __name__ == "__main__":
    shopping_cart = [
        Product("Laptop", 1200.0),
        Product("Smartphone", 699.99),
        Product("Headphones", 99.95)
    ]

    print("Shopping Cart Contents:")
    for product in shopping_cart:
        print(f"{product.product_name}: ${product.price}")

    print(f"\nTotal Cost: ${total_cost(shopping_cart)}")
