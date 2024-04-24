#!/usr/bin/python3
"""Annotate the below function’s parameters and return values with the appropriate types"""


from typing import List, Tuple, Sequence, Union, Any


def element_length(lst: Sequence[Union[List[Any], Tuple[Any, ...]]]) -> List[int]:
    """Annotate the below function’s parameters and return values with the appropriate types"""
    return [len(i) for i in lst]
