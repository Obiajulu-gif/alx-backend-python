#!/usr/bin/env python3
"""
1. Async Comprehensions
"""
from 0-async_generator import async_generator

async def async_comprehension():
    
    return [number async for number in async_generator()]
