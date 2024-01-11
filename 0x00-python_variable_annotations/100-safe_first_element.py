#!/usr/bin/env python3
'''
This module holds function that checks for the first element in an
input, but it has to be safe annotated first before operations can
pull through.
'''
from typing import Sequence, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    This function returns the first element of a sequence
    '''
    if lst:
        return lst[0]
    else:
        return None
