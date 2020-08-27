# -*- coding: utf-8 -*-
"""
    :author: T8840
"""

from typing import Dict, List, Optional, Sequence, Set, Tuple, Union
from pydantic import BaseModel


class Model(BaseModel):
    simple_list: list = None
    list_of_ints: List[int] = None

    simple_tuple: tuple = None
    tuple_of_different_types: Tuple[int, float, str, bool] = None

    simple_dict: dict = None
    dict_str_float: Dict[str, float] = None

    simple_set: set = None
    set_bytes: Set[bytes] = None

    str_or_bytes: Union[str, bytes] = None
    none_or_str: Optional[str] = None

    sequence_of_ints: Sequence[int] = None
    compound: Dict[Union[str, bytes], List[Set[int]]] = None


print(Model(simple_list=['1', '2', '3']).simple_list)  # > ['1', '2', '3']
print(Model(list_of_ints=['1', '2', '3']).list_of_ints)  # > [1, 2, 3]

print(Model(simple_tuple=(1, 2, 3, 4)).simple_tuple)  # > (1, 2, 3, 4)
print(Model(tuple_of_different_types=[1, 2.0, '3', True]).tuple_of_different_types)  # > (1, 2.0, '3', True)

print(Model(simple_dict={'a': 1, b'b': 2}).simple_dict)  # > {'a': 1, b'b': 2}
print(Model(dict_str_float={'a': 1, b'b': 2}).dict_str_float)  # > {'a': 1.0, 'b': 2.0}

print(Model(simple_set={1, 2, 3, 4}).simple_set)
print(Model(set_bytes={b'1', b'2', b'3', b'4'}).set_bytes)

print(Model(str_or_bytes='hello world').str_or_bytes)
print(Model(str_or_bytes=b'hello world').str_or_bytes)
print(Model(none_or_str='hello world').none_or_str)
print(Model(none_or_str=None).none_or_str)

print(Model(sequence_of_ints=[1, 2, 3, 4]).sequence_of_ints)  # > [1, 2, 3, 4]
print(Model(compound={'name': [{1, 2, 3}], b'entitlement': [{10, 5}]}).compound)
