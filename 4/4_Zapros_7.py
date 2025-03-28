# -*- coding: utf-8 -*-
"""
Created on Tue Jan  2 00:45:50 2024

@author: Admin
"""

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

# Функция для вычисления среднего балла студентов
def average_grade(students):
    return sum(student.grade for student in students) / len(students)

# Пример использования
if __name__ == "__main__":
    student_list = [
        Student("Alice", 85.0),
        Student("Bob", 92.5),
        Student("Charlie", 78.3),
        Student("David", 89.7)
    ]

    print("List of Students with Grades:")
    for student in student_list:
        print(f"{student.name}: {student.grade}")

    print(f"\nAverage Grade: {average_grade(student_list)}")
