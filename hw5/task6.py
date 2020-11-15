# -*- coding: utf-8 -*-
"""
Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""


def calculate_hours(file_path):
    """
    Calculate total hours by subject
    :param file_path: str
    :return: dict
    """
    result = {}
    try:
        with open(file_path, 'r') as f:
            for line in f:
                subject, numbers = line.split(':')
                subject_sum = sum(int(x.split('(')[0]) for x in numbers.split(' ') if len(x) and x != '—' and x != '-')
                result[subject] = subject_sum
    except Exception as err:
        print('Unexpected error:', err)
    return result


if __name__ == '__main__':
    from pprint import pprint
    res_dict = calculate_hours('task6_test.txt')
    pprint(res_dict, width=1)


def test_positive():
    import os
    test_file = '1.txt'
    test_content = "Информатика: 100(л) 50(пр) 20(лаб)\n" \
                   "Физика: 30(л) - 10(лаб)\n" \
                   "Физкультура: - 30(пр) -"
    with open(test_file, 'w') as f:
        f.write(test_content)

    assert calculate_hours(test_file) == {"Информатика": 170, "Физика": 40, "Физкультура": 30}
    os.remove(test_file)


def test_non_exists_file():
    assert {} == calculate_hours('1')


def test_empty_file():
    import os
    f_path = 'tmp'
    f = open(f_path, 'w')
    f.close()
    assert {} == calculate_hours(f_path)
    os.remove(f_path)
