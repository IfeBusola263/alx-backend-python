#!/usr/bin/env python3
'''
A module for asynchronous functions.
'''
import asyncio
from asyncio import Task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    '''
    This function returns an instance of the asyncio Task.
    '''
    return asyncio.create_task(wait_random(max_delay))
