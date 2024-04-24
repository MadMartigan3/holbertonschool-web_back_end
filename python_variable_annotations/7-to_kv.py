#!/usr/bin/python3
"""function to_kv which takes a string k and an int OR float v as arguments"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple containing k and the square of v"""
    return (k, v * v)
