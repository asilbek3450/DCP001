# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 11:17:02 2024

@author: Admin
"""

def main_map():
    phone_book = {"Alice": 123456, "Bob": 789012, "Charlie": 345678}

    print(f"Phone number of Bob: {phone_book.get('Bob')}")
    
    phone_book["David"] = 555555
    print(f"Updated phone book: {phone_book}")

if __name__ == "__main__":
    main_map()
