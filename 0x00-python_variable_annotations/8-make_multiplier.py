#!/usr/bin/env python3
'''
The module holds a function which is annotated.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    The function takes a float and returns a function which takes a float
    and multiplies it by the float(multiplier).
    '''
    def multiply(mult):
        '''
        The Function to be returned
        '''
        return mult * multiplier

    return multiply
