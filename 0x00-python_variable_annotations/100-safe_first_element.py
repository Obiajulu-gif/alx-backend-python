#!/usr/bin/env python3
"""
10. Duck typing - first element of a sequence
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of a
    sequence if it exists, otherwise returns None.
    """
    if lst:
        return lst[0]
    else:
        return None
