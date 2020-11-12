# -*- coding: utf-8 -*-
"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""


def calculate_salary(production, rate, prize):
    """
    
    :param production: int 
    :param rate: float
    :param prize: float
    :return: float
    """
    return production * rate + prize


if __name__ == '__main__':
    from sys import argv
    try:
        print(f'Calculated salary: {calculate_salary(*map(float, argv[1:]))}')
    except Exception as err:
        print(f'Unexpected error: {err}')
