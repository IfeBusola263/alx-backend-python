#!/usr/bin/env python3
'''
Module for Asynchronous functions.
'''

import random
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    The function returns a list of delays in ascending order. That
    spawns another async function `wait_random` for n times.
    '''
    list_of_delays = [await wait_random(max_delay) for i in range(n)]
    return sorted(list_of_delays)
