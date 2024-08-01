#!/usr/bin/env python3
"""
8. Complex types - functions
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float multiplier as an argument
    and returns a function that multiplies a
    float by the multiplier.
    """
    def multipler_function(value: float) -> float:
        return value * multiplier
    return multipler_function
