# -*- coding: utf-8 -*-
"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число,
месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию
числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных. """


class Date:
    __data = {'day': 1, 'month': 1, 'year': 2000}
    __format_str = '{:s}{:02d}-{:02d}-{:d}'

    def __init__(self, str_date=None):
        if str_date:
            dt = Date.convert(str_date)
            if Date.is_valid(dt):
                self.__data = dt

    @staticmethod
    def is_valid(data: dict):
        if not type(data) is dict:
            return False
        if not data.keys() == Date.__data.keys():
            return False
        if data['day'] < 1 or data['day'] > 31 or data['month'] < 1 or data['month'] > 12 or data['year'] < 0:
            return False
        return True

    @classmethod
    def convert(cls, str_date):
        return {k: int(v) for k, v in zip(cls.__data.keys(), str_date.split('-'))}

    def __str__(self):
        return self.__format_str.format('', *self.__data.values())

    def __repr__(self):
        return self.__format_str.format('Date: ', *self.__data.values())


if __name__ == '__main__':
    d = Date('12-11-2020')
    print([d, d, d])
    print(d)

    a = Date.convert('12-11-2020')
    print(Date.is_valid(a))
    print(Date.is_valid({'day': 13, 'month': 13}))
    print(Date.is_valid({'day': 13, 'month': 13, 'year': 2000}))
    print(Date.is_valid({'day': 32, 'month': 12, 'year': 2000}))

    c = Date('1-1-0')
