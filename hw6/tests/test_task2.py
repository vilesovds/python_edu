# -*- coding: utf-8 -*-
import pytest
from task2 import Road


@pytest.mark.parametrize("length, width, density, thickness, expected", [
    # usual
    (500, 10, 9.35, 5.5, 257125.0),
    # one
    (1, 1, 1, 1, 1),
    # zero
    (500, 10, 9.35, 0, 0)])
def test_calc_mass_positive(length, width, density, thickness, expected):
    r = Road(length, width)
    assert expected == r.calc_mass(density, thickness)
