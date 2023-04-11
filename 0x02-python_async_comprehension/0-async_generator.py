#!/usr/bin/env python3
"""Coroutine that takes no arguments.
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Function that loops 10 times,each time asynchronously wait 1 second, 
       and yields a randon number
       between 0 and 10."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
