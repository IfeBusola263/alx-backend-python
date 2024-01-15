#!/usr/bin/env python3
'''
This module houses asynchronous functions.
'''


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''
    An async fucntion that waits for a random delay between
    0 and max_delay and returns it.
    '''
    r = random.uniform(0, max_delay)
    await asyncio.sleep(r)
    return r
