# -*- coding: utf-8 -*-
import random
"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


def write_numbers(file_path):
    """
    Generate some count of lines with numbers. Used random
    :param file_path: str
    :return:
    """
    count = random.randint(20, 40)
    try:
        with open(file_path, 'w') as f:
            for _ in range(count):
                f.write(' '.join([str(x) for x in random.sample(range(10, 90), random.randint(4, 12))]))
                f.write('\n')
    except Exception as err:
        print('Unexpected error:', err)


def calc_numbers(file_path):
    """
    Calculated total sum of numbers in file
    :param file_path: str
    :return: float
    """
    total = 0
    try:
        with open(file_path, 'r') as f:
            for line in f:
                try:
                    total += sum([float(x) for x in line.split()])
                except ValueError as err:
                    print('warning:', err)
    except Exception as err:
        print('Unexpected error:', err)
    return total


if __name__ == '__main__':
    file_name = 'task5_test.txt'
    write_numbers(file_name)
    print('Total count:', calc_numbers(file_name))
