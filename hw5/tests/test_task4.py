# -*- coding: utf-8 -*-
import pytest
import os
from task4 import translate_list


def test_non_exists_file(monkeypatch):
    out_print = []
    monkeypatch.setattr('builtins.print', lambda s: out_print.append(str(s)))
    translate_list('1', '2')
    assert out_print[0].startswith('Unexpected error: [Errno 2] No such file or directory:')


@pytest.mark.parametrize("content, expected", [
    # usual
    ("One - 1\nTwo - 2\nThree - 3\nFour - 4",
     'Один - 1\nДва - 2\nТри - 3\nЧетыре - 4'),
    # one
    ("One - 1", "Один - 1"),
    # empty
    ('', '')])
def test_content_list(content, expected):
    import os
    src_name = '1.txt'
    dst_name = '2.txt'
    with open(src_name, 'w') as f:
        f.write(content)
    translate_list(src_name, dst_name)
    with open(dst_name) as f:
        content = f.read()
    assert content == expected
    os.remove(src_name)
    os.remove(dst_name)
