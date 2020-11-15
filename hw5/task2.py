# -*- coding: utf-8 -*-
"""
Создать текстовый файл (не программно),
сохранить в нем несколько строк,
выполнить подсчет количества строк,
количества слов в каждой строке.
"""
FILENAME = 'task2_tmp.txt'


def calc_lines_words(file_path):
    """
    Calculate lines count and words count in each line
    :param file_path: path of file
    :return: dict
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
    num, counts = calc_lines_words(FILENAME)
    print(f'Found {num} line(s)')
    for k, v in counts.items():
        print(f'Line {k}: {v} word(s)')


def test_not_exists_file():
    assert (0, {}) == calc_lines_words('eee')


def test_empty_file():
    f = open(FILENAME, 'w')
    f.close()
    assert (0, {}) == calc_lines_words(FILENAME)


def test_few_lines():
    content = ['one\n', 'one two\n', 'one two three\n', '\n', 'one two three four five']
    with open(FILENAME, 'w') as f:
        f.writelines([x for x in content])
    res = {1: 1, 2: 2, 3: 3, 4: 0, 5: 5}
    assert (5, res) == calc_lines_words(FILENAME)
