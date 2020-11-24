# -*- coding: utf-8 -*-
"""
Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна. Проверить работу метода.
"""


class Road:
    """
    Storage length and width of real road.
    """
    __length = 0
    __width = 0

    def __init__(self, length, width):
        """
        :param length: number
        :param width: number
        """
        if length <= 0 or width <= 0:
            raise ValueError("length and width must be positive numbers", length, width)
        self.__length = length
        self.__width = width

    def calc_mass(self, density, thickness):
        """
        Mass calculation as w*l*h*rho
        :param density: number
        :param thickness: number
        :return: number, kg
        """
        if density <= 0 or thickness <= 0:
            raise ValueError("density and thickness must be positive numbers", density, thickness)
        return self.__width * self.__length * density * thickness


if __name__ == '__main__':
    road = Road(500, 10)
    print(f'total mass of asphalt {road.calc_mass(9.35, 5.5)} kg')
