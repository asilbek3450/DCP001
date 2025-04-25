# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 11:17:25 2024

@author: Admin
"""

def main_set():
    colors = {"Red", "Green", "Blue"}

    print(f"Is Yellow in the set? {'Yellow' in colors}")
    
    colors.add("Yellow")
    print(f"Updated colors set: {colors}")

if __name__ == "__main__":
    main_set()
