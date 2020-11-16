# -*- coding: utf-8 -*-
import pytest
import os
from task2 import calc_lines_words


def test_not_exists_file(monkeypatch):
    out_print = []
    monkeypatch.setattr('builtins.print', lambda s: out_print.append(str(s)))
    assert (0, {}) == calc_lines_words('')
    assert out_print[0].startswith('[Errno 2] No such file or directory:')


@pytest.mark.parametrize("content, expected", [
    # usual
    (['one\n', 'one two\n', 'one two three\n', 'one two three four\n'],
     (4, {1: 1, 2: 2, 3: 3, 4: 4})),
    # one
    (['one\n'],
     (1, {1: 1})),
    # hole ;)
    (['one\n', 'one two\n', 'one two three\n', ' \n', 'one two three four five'],
     (5, {1: 1, 2: 2, 3: 3, 4: 0, 5: 5})),
    # empty
    ([], (0, {}))])
def test_content_lines(content, expected):
    file_name = 'task2_tmp.txt'
    with open(file_name, 'w') as f:
        f.writelines([x for x in content])
    assert expected == calc_lines_words(file_name)
    os.remove(file_name)
