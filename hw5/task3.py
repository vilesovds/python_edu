# -*- coding: utf-8 -*-
"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""


def salary_analyze(file_path, salary_thr=20000.0):
    """
    Filter list of employees with salary threshold and calculate average salary
    :param file_path: path to file
    :param salary_thr: salary_threshold float
    :return: tuple of list and float
    """
    filtered_list = []
    salary_avr = 0
    items_count = 0
    try:
        with open(file_path, 'r') as f:
            for line in f:
                try:
                    name, salary = line.split(':')
                    salary = float(salary)
                    salary_avr += salary
                    items_count += 1
                    if salary < salary_thr:
                        filtered_list.append(name)
                except ValueError:
                    print('Found some wrong data at line:', line)
    except Exception as err:
        print(err)
    salary_avr = salary_avr / items_count if items_count else 0
    return filtered_list, salary_avr


if __name__ == '__main__':
    thr = 20000.0
    li, avr = salary_analyze('task3_tmp.txt', thr)
    if len(li):
        print(f'People, who has salary lower than {thr}:')
        for p in li:
            print('\t', p)
    else:
        print(f'There are no one who has salary lower than {thr}:')

    print(f'Salary average is {avr}')
