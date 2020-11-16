# -*- coding: utf-8 -*-
"""
Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке.
"""


def calc_lines_words(file_path):
    """
    Calculate lines count and words count in each line
    :param file_path: path of file
    :return: tuple of int and dict
    """
    result = dict()
    line_num = 0
    try:
        with open(file_path, 'r') as f:
            for line_num, fl in enumerate(f, 1):
                result[line_num] = fl.count(' ') + 1 if fl != '\n' else 0
    except Exception as err:
        print(err)
    return line_num, result


if __name__ == '__main__':
    num, counts = calc_lines_words('task2_tmp.txt')
    print(f'Found {num} line(s)')
    for k, v in counts.items():
        print(f'Line {k}: {v} word(s)')
