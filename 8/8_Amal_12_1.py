# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 14:32:22 2024

@author: Admin
"""

import threading

def child_thread(mvar):
    for _ in range(3):
        print("Child thread incrementing")
        with mvar:
            mvar[0] += 1

if __name__ == "__main__":
    mvar = threading.Lock()
    mvar_value = [0]
    print("Start main thread")
    thread = threading.Thread(target=child_thread, args=(mvar_value,))
    thread.start()
    for _ in range(3):
        print("Main thread reading")
        with mvar:
            value = mvar_value[0]
        print(f"Main thread value: {value}")
    thread.join()
