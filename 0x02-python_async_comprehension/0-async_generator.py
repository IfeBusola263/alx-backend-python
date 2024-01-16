#!/usr/bin/env python3
'''
A module for coroutines
'''
import random
import asyncio


async def async_generator() -> float:
    '''
    The generator function returns a random number between
    0 and 10.
    '''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
