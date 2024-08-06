#!/usr/bin/env python3
"""
1. Async Comprehensions
"""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    '''make a list of 10 num from imported generator
    '''
    return [number async for number in async_generator()]
