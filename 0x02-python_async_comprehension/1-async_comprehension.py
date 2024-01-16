#!/usr/bin/env python3
'''
A module for coroutines.
'''
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    This coroutine uses async comprehension to collect data from
    a generator.
    '''
    num_list = [i async for i in async_generator()]
    return num_list
