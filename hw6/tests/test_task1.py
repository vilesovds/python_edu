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


class MockTrafficLight:

    def __init__(self, counts, **kwargs):
        self.tc = TrafficLight(**kwargs)
        self.prints = []
        self.counts = counts

    def stop_when_done(self, *args):
        if self.counts:
            self.counts -= 1
        else:
            # to stop forever loop
            raise Exception

    def mock_print(self, *args):
        self.prints.extend(map(str, args))

    def get_printed(self):
        return '\n'.join(self.prints)


@pytest.mark.parametrize('counts, kwargs, expected', [
    # usual
    (3, {'red': 1, 'yellow': 2, 'green': 3}, 'red will be on for 1 sec(s)\n1\nyellow will be on for 2 sec(s)\n2\n1\n'
                                             'green will be on for 3 sec(s)\n3'),
    # 2 times
    (9, {'red': 1, 'yellow': 2, 'green': 3},
     'red will be on for 1 sec(s)\n1\nyellow will be on for 2 sec(s)\n2\n1\n'
     'green will be on for 3 sec(s)\n3\n2\n1\n'
     'red will be on for 1 sec(s)\n1\nyellow will be on for 2 sec(s)\n2\n1\n'
     'green will be on for 3 sec(s)\n3')
])
def test_traffic_light_running(monkeypatch, counts, kwargs, expected):
    tts = MockTrafficLight(counts, **kwargs)
    monkeypatch.setattr("task1.sleep", tts.stop_when_done)
    monkeypatch.setattr('builtins.print', tts.mock_print)
    with pytest.raises(Exception):
        tts.tc.running()
    assert tts.get_printed() == expected
