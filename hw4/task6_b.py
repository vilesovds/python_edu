# -*- coding: utf-8 -*-
from itertools import cycle
"""
итератор, повторяющий элементы некоторого списка, определенного заранее. Использовать функцию cycle
"""


def list_repeater_generator(src_list):
    """
    Repeat elements from src_list
    :param src_list: list
    :return: one of element from src_list
    """
    for el in cycle(src_list):
        yield el


# let's try next() method this time
gen = list_repeater_generator(['a', 'b', 'c'])
for i in range(10):
    print(next(gen))
