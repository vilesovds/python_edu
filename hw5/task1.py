# -*- coding: utf-8 -*-
"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""


def collaborate(file_path):
    with open(file_path, 'w') as f:
        while True:
            i = input("Please enter some string or type Enter to exit: ")
            if not i:
                break
            print(i, file=f)


if __name__ == '__main__':
    collaborate('task1_tmp.txt')
