# -*- coding: utf-8 -*-
import pytest
import os
from task3 import salary_analyze


def test_non_exists_file(monkeypatch):
    out_print = []
    monkeypatch.setattr('builtins.print', lambda s: out_print.append(str(s)))
    assert ([], 0) == salary_analyze('1')
    assert out_print[0].startswith('[Errno 2] No such file or directory:')


@pytest.mark.parametrize("content, expected", [
    # usual
    (['Ivanov:20000\n',
      'Petrov:10000\n',
      'Sidorov:15000\n',
      'Medvedev:150000\n'], (['Petrov', 'Sidorov'], 48750.0)),
    # one
    (['Ivanov:20000\n'], ([], 20000.0)),
    # empty line
    (['Ivanov:20000\n',
      'Petrov:10000\n',
      '\n',
      'Medvedev:150000\n'], (['Petrov'], 60000.0)),
    # not a number value
    (['Ivanov:20000\n',
      'Petrov:10000\n',
      'Sidorov:eee\n',
      'Medvedev:150000\n'], (['Petrov'], 60000)),
    # empty
    ([''], ([], 0))])
def test_content_list(content, expected):
    f_path = 'tmp'
    with open(f_path, 'w') as f:
        f.writelines(content)
    assert expected == salary_analyze(f_path)
    os.remove(f_path)
