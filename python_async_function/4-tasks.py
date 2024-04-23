#!/usr/bin/python3
"""Write an asynchronous coroutine that takes in an integer argument"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a list of delays in ascending order"""
    delays = [task_wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]
