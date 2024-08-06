#!/usr/bin/env python3
"""The Basic of Async"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    the basic of async
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
