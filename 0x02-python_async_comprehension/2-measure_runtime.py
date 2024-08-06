#!/usr/bin/env python3
"""
2. Run time for four parallel comprehensions
"""
from time import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Check execution time
    """
    start = time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time() - start
