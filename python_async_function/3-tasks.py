#!/usr/bin/env python3
"""Write an asynchronous coroutine that takes in an integer argument"""

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns a asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))
