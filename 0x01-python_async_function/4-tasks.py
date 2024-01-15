#!/usr/bin/env python3
'''
Module for Asynchronous functions.
'''

import random
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    The function returns a list of delays in ascending order. That
    spawns another async function `task_wait_random` for n times.
    '''
    list_of_delays = [await task_wait_random(max_delay) for i in range(n)]
    return sorted(list_of_delays)
