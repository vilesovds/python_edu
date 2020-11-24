# -*- coding: utf-8 -*-
import pytest
from task7 import generate_sample_file
from task7 import calculate_profit
import os
import json


@pytest.mark.parametrize("name, samples", [('task7_test.txt', [("firm_1", "ООО", 10000, 5000),
                                                               ("firm_2", "Gmbh", 20000, 7000)])])
def test_generate_sample_file(name, samples):
    generate_sample_file(name, samples)
    assert os.path.exists(name)
    content_gen = ([str(y) for y in x] for x in samples)
    with open(name, 'r') as f:
        for s, content in zip(content_gen, f):
            fs = list(content[:-1].split(' '))
            assert s == fs
    os.remove(name)


@pytest.mark.parametrize("src_name, dst_name, samples, expected", [
    # one negative
    ('task7_test.txt', 'task7_test.json',
     [("firm_1", "OOO", 10000, 5000),
      ("firm_2", "Gmbh", 20000, 7000),
      ("firm_3", "LLC", 8000, 28000)],
     '[{"firm_3": -20000, "firm_2": 13000, "firm_1": 5000}, {"average_profit": 9000}]'),
    # all positive
    ('task7_test.txt', 'task7_test.json',
     [("firm_1", "OOO", 10000, 5000),
      ("firm_2", "Gmbh", 20000, 7000),
      ("firm_3", "LLC", 20000, 8000)],
     '[{"firm_3": 12000, "firm_2": 13000, "firm_1": 5000}, {"average_profit": 10000}]')
])
def test_samples(src_name, dst_name, samples, expected):
    generate_sample_file(src_name, samples)
    calculate_profit(src_name, dst_name)
    with open(dst_name, 'r') as f:
        js = json.load(f)
    js_exp = json.loads(expected)
    assert js_exp == js

    os.remove(src_name)
    os.remove(dst_name)


@pytest.mark.parametrize("src_name, dst_name, samples, expected", [('', '2', [], FileNotFoundError),
                                                                   ('1', '2', ['a'], ValueError),
                                                                   ('1', '2', [("a", "b", 1000, "trash")], ValueError)])
def test_exceptions(src_name, dst_name, samples, expected):
    try:
        os.remove(dst_name)
    except Exception:
        pass
    try:
        os.remove(src_name)
    except Exception:
        pass

    with pytest.raises(expected):
        if src_name:
            generate_sample_file(src_name, samples)
        calculate_profit(src_name, dst_name)

    try:
        os.remove(src_name)
    except Exception:
        pass
    try:
        os.remove(dst_name)
    except Exception:
        pass
