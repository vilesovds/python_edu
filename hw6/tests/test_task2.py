# -*- coding: utf-8 -*-
import pytest
from task2 import Road


@pytest.mark.parametrize("length, width, density, thickness, expected", [
    # usual
    (500, 10, 9.35, 5.5, 257125.0),
    # one
    (1, 1, 1, 1, 1)])
def test_calc_mass_positive(length, width, density, thickness, expected):
    r = Road(length, width)
    assert expected == r.calc_mass(density, thickness)


@pytest.mark.parametrize("length, width, expected", [(-2, 0, ValueError),
                                                     (2, -1, ValueError),
                                                     (-2, 1, ValueError),
                                                     (0, 0, ValueError),
                                                     ('2', 1, TypeError)])
def test_exceptions_init(length, width, expected):
    with pytest.raises(expected):
        Road(length, width)


@pytest.mark.parametrize("density, thickness, expected", [(0, 0, ValueError),
                                                          (-1, 200, ValueError),
                                                          (10, -1, ValueError),
                                                          ('2', 200, TypeError)])
def test_exceptions_calc(density, thickness, expected):
    with pytest.raises(expected):
        r = Road(10, 100)
        r.calc_mass(density, thickness)
