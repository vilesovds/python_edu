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
                    salary = float(salary[:-1])
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


def test_non_exists_file():
    assert ([], 0) == salary_analyze('1')


def test_empty_file():
    import os
    f_path = 'tmp'
    f = open(f_path, 'w')
    f.close()
    assert ([], 0) == salary_analyze(f_path)
    os.remove(f_path)


def test_positive():
    import os
    content = ['Ivanov:20000\n',
               'Petrov:10000\n',
               'Sidorov:15000\n',
               'Medvedev:150000\n']
    li = ['Petrov', 'Sidorov']
    fs = 48750.0
    f_path = 'tmp'
    with open(f_path, 'w') as f:
        f.writelines(content)

    assert (li, fs) == salary_analyze(f_path)

    os.remove(f_path)


def test_empty_line():
    import os
    content = ['Ivanov:20000\n',
               'Petrov:10000\n',
               '\n',
               'Medvedev:150000\n']
    li = ['Petrov']
    fs = 60000.0
    f_path = 'tmp'
    with open(f_path, 'w') as f:
        f.writelines(content)

    assert (li, fs) == salary_analyze(f_path)
    os.remove(f_path)


def test_not_a_number_value():
    import os
    content = ['Ivanov:20000\n',
               'Petrov:10000\n',
               'Sidorov:eee\n',
               'Medvedev:150000\n']
    li = ['Petrov']
    fs = 60000.0
    f_path = 'tmp'
    with open(f_path, 'w') as f:
        f.writelines(content)

    assert (li, fs) == salary_analyze(f_path)
    os.remove(f_path)
