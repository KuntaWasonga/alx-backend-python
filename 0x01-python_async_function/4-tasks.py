#!/usr/bin/env python3
"""Defines"""
from typing import List
import asyncio

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Function that takes code from wait_n and alters it to new function"""
    tasks = await asyncio.gather(*tuple(map(lambda _:task_wait_random(max_delay), range(n))))
    return sorted(tasks)
