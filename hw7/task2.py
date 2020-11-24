# -*- coding: utf-8 -*-
"""
Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    name = 'Some'

    @property
    @abstractmethod
    def fabric_consumption(self):
        pass

    @staticmethod
    def calc_fabric_consumption(closes):
        """
        Helper to calculate total fabric consumption
        :param closes: list of Closes
        :return: float
        """
        return sum(map(float, closes))

    def __float__(self):
        return self.fabric_consumption

    def __mul__(self, other):
        """
        Create list of objects * other as count
        :param other: int
        :return: list
        """
        if type(other) == int:
            return [self for _ in range(other)]

    def __repr__(self):
        return self.name


class Coat(Clothes):
    _minimum_size = 32

    def __init__(self, size, name='Coat'):
        if size < self._minimum_size:
            raise ValueError(f"Size couldn't be lower than {self._minimum_size}")
        self.size = size
        self.name = name

    @property
    def fabric_consumption(self):
        return self.size/6.5 + 0.5


class Suit(Clothes):
    _minimum_height = 100

    def __init__(self, height, name="Suit"):
        if height < self._minimum_height:
            raise ValueError(f"Height couldn't be lower than {self._minimum_height}")
        self.height = height
        self.name = name

    @property
    def fabric_consumption(self):
        return 2 * self.height + 0.3


if __name__ == '__main__':
    s = Suit(80)
    print(f'{s} takes {s.fabric_consumption}')
    c = Coat(42)
    print(f'{c} takes {c.fabric_consumption}')
    print(c*10 + s*12)
    print(Clothes.calc_fabric_consumption(c*10 + s*12))
