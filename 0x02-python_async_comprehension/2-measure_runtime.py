#!/usr/bin/env python3
'''
A module for coroutines
'''
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    The coroutine returns time for all the session to run.
    '''
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         )
    elapsed = time.perf_counter() - start
    return elapsed
