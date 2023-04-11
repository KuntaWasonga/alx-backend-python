#!/usr/bin/env python3
"""Coroutine that executes other function."""
import time
import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Coroutine that executes async_comprehension four times in parallel
        using asyncio.gather."""
    tasks = []
    start = time.time()
    for i in range(4):
        tasks.append(asyncio.create_task(async_comprehension()))
    await asyncio.gather(*tasks)
    end = time.time()

    return end - start
