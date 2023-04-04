#!/usr/bin/env python3
"""Module executing wait_n."""
from typing import List
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function that executes wait_randon n times."""
    tasks = await asyncio.gather(*tuple(map(lambda _:wait_random(max_delay), range(n))))
    return sorted(tasks)
