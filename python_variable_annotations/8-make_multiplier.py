#!/usr/bin/env python3
"""function make_multiplier that takes a float
multiplier as argument and returns a function"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function make_multiplier that takes a float
    multiplier as argument and returns a function"""
    def multiply(n: float) -> float:
        """function multiply that takes a float n
        as argument and returns a float"""
        return n * multiplier
    return multiply
