#!/usr/bin/env python3
"""
12. Type Checking
"""
from typing import List, Union, Tuple


def zoom_array(lst: Union[List[int], Tuple[int, ...]],
               factor: int = 2) -> List[int]:
    """
    Use mypy to validate the following piece of code
    and apply any necessary changes.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
