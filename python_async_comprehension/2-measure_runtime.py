#!/usr/bin/env python3
"""measure_runtime should measure the total runtime and return it."""

import asyncio
from time import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime should measure the total runtime and return it."""
    start = time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = time()
    return end - start
