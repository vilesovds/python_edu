# -*- coding: utf-8 -*-
import pytest
import os
from task5 import calc_numbers


@pytest.mark.parametrize("content, expected", [
    # usual
    ('1 12 14\n 2 22 44\n1 2 3 4 5 6 7', 123.0),
    # float
    ('1.2 2.8\n 2.0 3.5', 9.5),
    # mix int and float
    ('1.2 2\n 4 3.5', 10.7),
    # one
    ('1', 1),
    # zero
    ('', 0)])
def test_positive_content(content, expected):
    test_file = 'tmp'
    with open(test_file, 'w') as f:
        f.write(content)

    assert calc_numbers(test_file) == expected
    os.remove(test_file)


@pytest.mark.parametrize("content, expected, message", [
    # empty line
    ('1 12 14\n\n\n1 2 3 4 5 6 7', 55, ''),
    # not a number
    ('1 12 14\naaa aa\n\n1 2 3 4 5 6 7', 55, 'warning: could not convert string to float:')])
def test_negative_content(monkeypatch, content, expected, message):
    out_print = []
    monkeypatch.setattr('builtins.print', lambda *args: out_print.extend(map(str, args)))
    test_file = 'tmp'

    with open(test_file, 'w') as f:
        f.write(content)

    assert calc_numbers(test_file) == expected
    assert ' '.join(out_print).startswith(message)
    os.remove(test_file)


def test_non_exists_file(monkeypatch):
    out_print = []
    monkeypatch.setattr('builtins.print', lambda *args: out_print.extend(map(str, args)))
    assert 0 == calc_numbers('')
    assert ' '.join(out_print).startswith('Unexpected error: [Errno 2] No such file or directory:')
