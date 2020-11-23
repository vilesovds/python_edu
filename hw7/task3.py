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
        # todo check number
        self.count = count

    def __add__(self, other):
        # todo check other type
        return CellStorage(self.count + other.count)

    def __sub__(self, other):
        # todo check other type
        if self.count - other.count <= 0:
            raise ValueError('Difference between cells counters should be more than zero', self.count, other.count)
        return CellStorage(self.count - other.count)

    def __mul__(self, other):
        # todo check other type
        return CellStorage(self.count * other.count)

    def __truediv__(self, other):
        # todo check other type
        # todo check zero
        return CellStorage(self.count//other.count)

    def make_order(self, cells_in_row):
        # todo check zero
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
