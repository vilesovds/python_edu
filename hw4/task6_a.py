# -*- coding: utf-8 -*-
from itertools import count
"""
итератор, генерирующий целые числа, начиная с указанного, используя функцию count()
"""


def even_number_generator(from_number):
    """
    Generate even number. Start from from_number
    :param from_number: int
    :return: even integer
    """
    for el in count(from_number):
        if not el & 0x01:
            yield el


start = 8
stop = 18

for i in even_number_generator(start):
    print(i)
    if i >= stop:
        break
