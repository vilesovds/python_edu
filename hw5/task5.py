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
                total += sum([float(x) for x in line.split()])
    except Exception as err:
        print('Unexpected error:', err)
    return total


if __name__ == '__main__':
    file_name = 'task5_test.txt'
    write_numbers(file_name)
    print('Total count:', calc_numbers(file_name))


def test_write_non_empty_file():
    import os
    test_file = '1'
    write_numbers(test_file)

    assert os.path.getsize(test_file)
    os.remove(test_file)


def test_positive():
    import os
    test_file = '1.txt'
    test_content = '1 12 14\n 2 22 44\n1 2 3 4 5 6 7'
    with open(test_file, 'w') as f:
        f.write(test_content)

    assert calc_numbers(test_file) == 123.0
    os.remove(test_file)


def test_empty_line():
    import os
    test_file = '1.txt'
    test_content = '1 12 14\n\n\n1 2 3 4 5 6 7'
    with open(test_file, 'w') as f:
        f.write(test_content)

    assert calc_numbers(test_file) == 55.0
    os.remove(test_file)


def test_non_exists_file():
    assert 0 == calc_numbers('1')


def test_empty_file():
    import os
    f_path = 'tmp'
    f = open(f_path, 'w')
    f.close()
    assert 0 == calc_numbers(f_path)
    os.remove(f_path)
