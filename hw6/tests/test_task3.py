# -*- coding: utf-8 -*-
import pytest
from task3 import Worker, Position


@pytest.mark.parametrize("name, surname, position, wage, bonus, expected", [
    # usual
    ('Ivan', 'Petrov', 'Teacher', 15550, 520, ('Ivan', 'Petrov', 'Teacher', {'wage': 15550, 'bonus': 520})),
    # one
    ('', '', '', 0, 0, ('', '', '', {'wage': 0, 'bonus': 0}))])
def test_create(name, surname, position, wage, bonus, expected):
    p = Position(name, surname, position, wage, bonus)
    assert expected == (p.name, p.surname, p.position, p._income)


@pytest.mark.parametrize("wage, bonus, expected", [
    # usual
    (15550, 520, 16070),
    # zero
    (0, 0, 0)])
def test_total_income(wage, bonus, expected):
    p = Position('A', 'B', 'C', wage, bonus)
    assert expected == p.get_total_income()


@pytest.mark.parametrize("name, surname, expected", [
    # usual
    ('Ivan', 'Bespaly', 'Ivan Bespaly'),
    # zero
    ('', '', ' ')])
def test_get_full_name(name, surname, expected):
    p = Position(name, surname, 'C', 11, 0)
    assert expected == p.get_full_name()

