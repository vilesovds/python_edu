# -*- coding: utf-8 -*-
import pytest
import os
from task6 import calculate_hours


@pytest.mark.parametrize("content, expected", [
    # usual
    ("Информатика: 100(л) 50(пр) 20(лаб)\n" \
     "Физика: 30(л) - 10(лаб)\n" \
     "Физкультура: - 30(пр) -", {"Информатика": 170, "Физика": 40, "Физкультура": 30}),
    # one
    ("Информатика: 100(л) - -\n",
     {"Информатика": 100}),
    # no hours
    ("Информатика: - - -\n" \
     "Физика: - - -\n" \
     "Физкультура: - - -", {"Информатика": 0, "Физика": 0, "Физкультура": 0}),
    # empty
    ('', {})])
def test_content_list(content, expected):
    test_file = '1.txt'
    with open(test_file, 'w') as f:
        f.write(content)

    assert calculate_hours(test_file) == expected
    os.remove(test_file)


def test_non_exists_file(monkeypatch):
    out_print = []
    monkeypatch.setattr('builtins.print', lambda *args: out_print.extend(map(str, args)))
    assert {} == calculate_hours('1')
    assert ' '.join(out_print).startswith('Unexpected error: [Errno 2] No such file or directory:')


@pytest.mark.parametrize("content, expected, message", [
    # not a number
    ("Информатика: 100(л) eee(пр) -\n",
     {},
     'Unexpected error: invalid literal for int() with base 10:'),
    # no subject
    ("Физика: 30(л) - 10(лаб)\n" \
     "100(л) 50(пр) -\n",
     {"Физика": 40},
     'Unexpected error: not enough values to unpack')])
def test_wrong_content_list(monkeypatch, content, expected, message):
    out_print = []
    monkeypatch.setattr('builtins.print', lambda *args: out_print.extend(map(str, args)))

    test_file = 'tmp'
    with open(test_file, 'w') as f:
        f.write(content)
    assert expected == calculate_hours(test_file)
    assert ' '.join(out_print).startswith(message)
    os.remove(test_file)
