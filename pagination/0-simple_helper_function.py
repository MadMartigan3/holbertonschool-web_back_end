#!/usr/bin/env python3
"""function named index_range that takes two integer arguments"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """function named index_range that takes two integer arguments"""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
