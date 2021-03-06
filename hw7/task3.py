# -*- coding: utf-8 -*-
"""
Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
обычное (не целочисленное) деление клеток, соответственно.
В методе деления должно осуществляться округление значения до целого числа.

Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток больше
нуля, иначе выводить соответствующее сообщение.

Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек этих
двух клеток.

Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
 ячеек этих двух клеток.

В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный метод
позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order()
вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order()
вернет строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке.
"""


class CellStorage:

    def __init__(self, count: int):
        if not type(count) is int:
            raise TypeError(f'Count should be an natural number but got {type(count)}')
        if count < 0:
            raise ValueError(f'Count should greater or equal zero but got {type(count)}')
        self.count = count

    @classmethod
    def __check_other(cls, other):
        if not type(other) is cls:
            raise TypeError(f'Only {cls.__name__} supported but got {type(other)}')

    def __add__(self, other):
        self.__check_other(other)
        return CellStorage(self.count + other.count)

    def __sub__(self, other):
        self.__check_other(other)
        return CellStorage(self.count - other.count)

    def __mul__(self, other):
        self.__check_other(other)
        return CellStorage(self.count * other.count)

    def __truediv__(self, other):
        self.__check_other(other)
        return CellStorage(self.count//other.count)

    def make_order(self, cells_in_row):
        end = self.count + self.count // cells_in_row + 1  # count of * + count of \n + border
        return ''.join('\n' if not x % (cells_in_row + 1) else '*' for x in range(1, end))

    def __repr__(self):
        return f'CellStorage({self.count})'


if __name__ == '__main__':
    storage = CellStorage(17)
    st2 = CellStorage(2)
    print(storage / st2)
    print(storage - st2)
    print(storage + st2)
    print(storage * st2)

    print(storage.make_order(5))
    print('-'*17)

    print(storage.make_order(7))
    print('-'*17)
    print(storage.make_order(17))
    print('-' * 17)


