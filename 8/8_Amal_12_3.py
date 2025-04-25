# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 14:26:41 2024

@author: Admin
"""

import threading
import time

def child_thread():
    for _ in range(3):
        print("Child thread")
        time.sleep(1)

if __name__ == "__main__":
    print("Start main thread")
    thread = threading.Thread(target=child_thread)
    thread.start()
    for _ in range(3):
        print("Main thread")
        time.sleep(1)
    thread.join()
