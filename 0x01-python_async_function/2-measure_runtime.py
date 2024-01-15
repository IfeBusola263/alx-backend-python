#!/usr/bin/env python3
'''
A module for asynchronous functions.
'''
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    The functions returns the total time of execution on the
    async function `wait_n`. given the number of spawn(n),
    and the maximum delay(max_delay).
    '''
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - start
    return elapsed / n
