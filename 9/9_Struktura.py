# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 14:01:42 2024

@author: Admin
"""

# Определение класса для точки в трехмерном пространстве
class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

# Функция, принимающая аргумент типа Point3D
def print_point(point):
    print(f"Точка в трехмерном пространстве: ({point.x}, {point.y}, {point.z})")

# Использование функции с различными объектами, совместимыми по структуре
point_a = Point3D(1.0, 2.0, 3.0)
point_b = Point3D(4.0, 5.0, 6.0)

# Оба вызова функции будут успешными, так как объекты совместимы по структуре
print_point(point_a)
print_point(point_b)
