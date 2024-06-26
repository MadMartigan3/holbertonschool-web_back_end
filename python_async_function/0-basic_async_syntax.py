#!/usr/bin/env python3
"""Write an asynchronous coroutine that takes in an integer argument"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Asynchronous coroutine that takes in an integer argument"""
    await asyncio.sleep(random.uniform(0, max_delay))
    return random.uniform(0, max_delay)
