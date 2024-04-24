#!/usr/bin/python3
"""Write an asynchronous coroutine that takes in an integer argument"""

import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int = 0, max_delay: int = 10) -> float:
    """Measures the runtime of wait_random n times"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()

    return ((end - start) / n)
