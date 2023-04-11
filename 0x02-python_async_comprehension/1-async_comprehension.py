#!/usr/bin/env python3
"""Coroutine that takes no arguments."""
from typing import List
import asyncio

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Coroutine that collects 10 randon numbers
       then returns the 10 random numbers."""
    return [i async for i in async_generator()]
