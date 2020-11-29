# -*- coding: utf-8 -*-
"""Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка. Примечание: длина списка не фиксирована.
Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта, введя, например,
команду “stop”. При этом скрипт завершается, сформированный список выводится на экран. Подсказка: для данного задания
примем, что пользователь может вводить только числа и строки. При вводе пользователем очередного элемента необходимо
реализовать проверку типа элемента и вносить его в список, только если введено число. Класс-исключение должен не
позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. При этом работа скрипта не
должна завершаться. """


class NumbersOnly(Exception):
    def __init__(self, *args):
        self.txt = ' '.join(str(x) for x in args)

    def __str__(self):
        return self.txt


class CheckedList:
    _exception = NumbersOnly('only numbers are supported')
    __list = []
    # int should be the first
    supported_types = (int, float)

    def append(self, data):
        """
        Added one element
        :param data: number or string representation of a number
        :return: None
        """
        t = type(data)
        if t in self.supported_types:
            self.__list.append(data)
            return
        elif t == str:
            for f in self.supported_types:
                try:
                    num = f(data)
                except ValueError:
                    continue
                else:
                    self.__list.append(num)
                    return

        raise self._exception

    @property
    def numbers_list(self):
        return self.__list

    def __str__(self):
        return str(self.numbers_list).strip('[]')


if __name__ == '__main__':
    cl = CheckedList()
    while True:
        ui = input("Please input number: ")
        if not ui:
            break
        try:
            cl.append(ui)
        except NumbersOnly as err:
            print(f'Input error: {err}')
    print(f'Result: {cl}')
