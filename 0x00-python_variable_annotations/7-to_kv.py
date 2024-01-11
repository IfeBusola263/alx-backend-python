#!/usr/bin/env python3
'''
This module houses a to_kv function.
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    The function returns a tuple from k and v.
    '''
    return k, v ** 2
