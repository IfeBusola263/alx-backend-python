#!/usr/bin/env python3
'''
This module houses a function that takes a Maplike argument and returns
the value of the dictionary.
'''
from typing import Mapping, Union, Any, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] =
                     None) -> Union[Any, T]:
    '''
    The function returns the value of the Mapper with the given key
    if it is in the Mapper, else it returns an unknown as given by
    default or None.
    '''
    if key in dct:
        return dct[key]
    else:
        return default
