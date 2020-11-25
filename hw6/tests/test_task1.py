# -*- coding: utf-8 -*-
import pytest
from task1 import TrafficLight


@pytest.mark.parametrize("red, yellow, green, expected", [
    # usual
    (2, 3, 4, {'red': 2, 'yellow': 3, 'green': 4}),
    # from text
    ('2', '3', '4', {'red': 2, 'yellow': 3, 'green': 4}),
    # from float
    (2.1, 3.1, 4.1, {'red': 2, 'yellow': 3, 'green': 4})])
def test_traffic_light_apply_times(red, yellow, green, expected):
    tc = TrafficLight(red=red, yellow=yellow, green=green)

    assert tc._TrafficLight__times == expected


@pytest.mark.parametrize("red, yellow, green, kwargs, expected", [
    # zero
    (0, 3, 4, {}, ValueError),
    # negative
    (2, -3, 4, {}, ValueError),
    # non integer
    ('a', 3, 4, {}, ValueError),
    # None
    (1, None, 4, {}, TypeError),
    # wrong keys
    (2, 3, 4, {'test': 'me'}, KeyError),
])
def test_traffic_light_apply_times_negative(red, yellow, green, kwargs, expected):
    with pytest.raises(expected):
        kwargs['red'] = red
        kwargs['yellow'] = yellow
        kwargs['green'] = green
        TrafficLight(**kwargs)
