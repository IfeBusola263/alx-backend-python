#!/usr/bin/env python3
'''
The module hold a function that returns a value
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int | float]]) -> float:
    '''
    The function takes a list of floats and ints and returns the sum.
    '''
    return sum(mxd_lst)
