#!/usr/bin/env python3
'''
This module houses a function that returns a list of items.
'''
from typing import List, Tuple, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List[Any]:
    '''
    This function returns a list of items in the given Tuple.
    based on the number of factors given, being 2 minimum.
    '''
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
