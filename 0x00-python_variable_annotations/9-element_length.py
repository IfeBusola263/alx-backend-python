#!/usr/bin/env python3
'''
This module house a function that returns a list of tuples.
'''
from typing import Sequence, List, Iterable, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
