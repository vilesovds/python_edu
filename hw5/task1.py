# -*- coding: utf-8 -*-
"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""

FILENAME = 'task1_tmp.txt'


def main():
    with open(FILENAME, 'w') as f:
        while True:
            i = input("Please enter some string or type Enter to exit")
            if i == '':
                break
            print(i, file=f)


if __name__ == '__main__':
    main()


def test_main_empty(monkeypatch):
    import os.path
    # simple empty mock
    monkeypatch.setattr('builtins.input', lambda _: '')
    main()
    assert os.path.isfile(FILENAME)
    assert os.path.getsize(FILENAME) == 0


def test_main_list(monkeypatch):
    import os.path
    test_content = ["Mark", "Antony", "Lisa"]
    # prepare test data
    gen_list = test_content.copy()
    gen_list.append('')
    gen = (x for x in gen_list)

    # list mock
    monkeypatch.setattr('builtins.input', lambda _: next(gen))

    main()
    assert os.path.isfile(FILENAME)
    with open(FILENAME, 'r') as f:
        # we should remove last \n symbol before compare
        assert [rl[:-1] for rl in f.readlines()] == test_content
    os.remove(FILENAME)
