# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 14:38:47 2024

@author: Admin
"""

import asyncio

async def async_thread():
    for _ in range(3):
        print("Async thread")
        await asyncio.sleep(1)

if __name__ == "__main__":
    print("Start main thread")
    loop = asyncio.get_event_loop()
    task = loop.create_task(async_thread())
    for _ in range(3):
        print("Main thread")
        loop.run_until_complete(asyncio.sleep(1))
    loop.run_until_complete(task)
