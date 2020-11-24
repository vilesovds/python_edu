import pytest
from task1 import collaborate


@pytest.mark.parametrize("input_list, expected", [(["Mark", "Antony", "Lisa", ''], 'Mark\nAntony\nLisa\n'),
                                                  (["Mark", ''], 'Mark\n'),
                                                  (["Mark", '', "Lisa", ''], 'Mark\n'),
                                                  ([''], '')])
def test_content_list(monkeypatch, input_list, expected):
    import os.path
    test_file = '1.txt'
    gen_list = input_list.copy()
    gen = (x for x in gen_list)

    # list mock
    monkeypatch.setattr('builtins.input', lambda _: next(gen))

    collaborate(test_file)

    assert os.path.isfile(test_file)
    with open(test_file, 'r') as f:
        assert f.read() == expected
    os.remove(test_file)


@pytest.mark.parametrize('filename, expected', [('', FileNotFoundError)])
def test_negative_file_error(filename, expected):
    with pytest.raises(expected):
        collaborate(filename)
