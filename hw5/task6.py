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


def to_number(text):
    """
    Search number(float or integer) at start of text.
    :param text: string
    :return: float int or None
    """
    approved = '012345678.'
    to_convert = []
    for ch in text:
        if ch not in approved:
            break
        to_convert.append(ch)

    if len(to_convert):
        if to_convert[-1] == '.':
            to_convert.pop()
        s_to_num = ''.join(to_convert)
        return float(s_to_num) if '.' in s_to_num else int(s_to_num)
    else:
        return 0


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
                subject_sum = sum(int(n) for word in numbers.split() for n in word.split('(') if n.isdigit())
                result[subject] = subject_sum
    except Exception as err:
        print('Unexpected error:', err)
    return result


if __name__ == '__main__':
    from pprint import pprint
    res_dict = calculate_hours('task6_test.txt')
    pprint(res_dict, width=1)
