#!/usr/bin/env python3
"""
7. Complex types - string and int/float to tuple
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string and an int/float,
    returns a tuple with the string and
    the square of the int/float as a float.
    """
    return (k, float(v ** 2))
