# -*- coding: utf-8 -*-
"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""


def translate_list(src_path, dst_path):
    """
    translation of numerals into Russian
    :param src_path: source file path
    :param dst_path: destination file path
    :return:
    """
    decoder = {'One': 'Один',
               'Two': 'Два',
               'Three': 'Три',
               'Four': 'Четыре'}
    try:
        with open(src_path, 'r') as src_f, open(dst_path, 'w') as dst_f:
            for line in src_f:
                dst_f.write(' '.join(decoder[word] if word in decoder.keys() else word for word in line.split(' ')))
    except Exception as err:
        print(f'Unexpected error: {err}')


def create_src_file(file_path):
    with open(file_path, 'w') as f:
        f.write('One - 1\nTwo - 2\nThree - 3\nFour - 4')


if __name__ == '__main__':
    import os.path
    src_name = 'task4_src.txt'
    dst_name = 'task4_dst.txt'

    if not os.path.exists(src_name):
        create_src_file(src_name)

    translate_list(src_name, dst_name)
