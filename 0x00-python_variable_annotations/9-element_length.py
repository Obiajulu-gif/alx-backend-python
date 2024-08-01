#!/usr/bin/env python3
"""
9. Let's duck type an iterable object
"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and
    returns a list of tuples,
    each containing a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
