# -*- coding: utf-8 -*-
import pytest
from task4 import WordSide, Car, TownCar, WorkCar


@pytest.mark.parametrize('side, turn, expect', [
    ('NORTH', 'left', 'WEST'),
    ('NORTH', 'Right', 'EAST'),
    ('west', 'Left', 'SOUTH'),
    ('WEST', 'right', 'NORTH'),
    ('south', 'LefT', 'EAST'),
    ('soUth', 'RIGHT', 'WEST'),
    ('EASt', 'LefT', 'NORTH'),
    ('EaSt', 'RIGht', 'SOUTH')])
def test_word_side_turn(side, turn, expect):
    ws = WordSide(side)
    ws.turn(turn)
    assert ws.side == expect


@pytest.mark.parametrize('side, turn, expected', [
    # wrong init
    ('aaa', 'left', TypeError),
    # wrong turn
    ('North', 'a', TypeError),
    # zero init
    ('', 'left', TypeError),
    # zero turn
    ('North', '', TypeError)])
def test_word_side_exception(side, turn, expected):
    with pytest.raises(expected):
        ws = WordSide(side)
        ws.turn(turn)


@pytest.mark.parametrize('side, expected', [('North', 'NORTH'),
                                            ('west', 'WEST'),
                                            ('south', 'SOUTH'),
                                            ('east', 'EAST')])
def test_car_set_direction(side, expected):
    c = Car('test')
    c.direction = side
    assert c._Car__current_direction.side == expected


@pytest.mark.parametrize('side, expected', [('1', TypeError),
                                            ('', TypeError)])
def test_car_set_direction_exception(side, expected):
    with pytest.raises(expected):
        c = Car('test')
        c.direction = side


@pytest.mark.parametrize('name, speed, expected', [
    # usual
    ('123', 10, '"123" started'),
    # float
    ('123', 115.6, '"123" started'),
    # zero speed
    ('test', 0, '"test" started'),
    # zero name
    ('', 123, '"" started')])
def test_car_go(monkeypatch, name, speed, expected):
    out_print = []
    monkeypatch.setattr('builtins.print', lambda *args: out_print.extend(map(str, args)))

    c = Car(name)
    c.go(speed)
    assert c.speed == speed
    assert expected == ' '.join(out_print)


@pytest.mark.parametrize('speed, expected', [
    # negative
    (-1, ValueError),
    # not a number
    ('test', TypeError)])
def test_car_go_exception(monkeypatch, speed, expected):
    out_print = []
    monkeypatch.setattr('builtins.print', lambda *args: out_print.extend(map(str, args)))
    with pytest.raises(expected):
        c = Car('test')
        c.go(speed)


@pytest.mark.parametrize('name, expected', [
    # usual
    ('123', '"123" stopped'),
    # empty
    ('', '"" stopped')])
def test_car_stop(monkeypatch, name, expected):
    out_print = []
    monkeypatch.setattr('builtins.print', lambda *args: out_print.extend(map(str, args)))
    c = Car(name, speed=40)
    c.stop()
    assert c.speed == 0
    assert ''.join(out_print) == expected


@pytest.mark.parametrize('direction, turn, expected_direction, expected_print', [
    ('NORTH', 'left', 'WEST', '"test" going to the WEST'),
    ('NORTH', 'Right', 'EAST', '"test" going to the EAST'),
    ('west', 'Left', 'SOUTH', '"test" going to the SOUTH'),
    ('WEST', 'right', 'NORTH', '"test" going to the NORTH'),
    ('south', 'LefT', 'EAST', '"test" going to the EAST'),
    ('soUth', 'RIGHT', 'WEST', '"test" going to the WEST'),
    ('EASt', 'LefT', 'NORTH', '"test" going to the NORTH'),
    ('EaSt', 'RIGht', 'SOUTH', '"test" going to the SOUTH')])
def test_car_turn(monkeypatch, direction, turn, expected_direction, expected_print):
    out_print = []
    monkeypatch.setattr('builtins.print', lambda *args: out_print.extend(map(str, args)))
    c = Car('test', direction=direction)
    c.turn(turn)
    assert c.direction == expected_direction
    assert ''.join(out_print) == expected_print


@pytest.mark.parametrize('turn, expected', [
    # wrong turn
    ('a', TypeError),
    # zero turn
    ('', TypeError)])
def test_car_turn_exception(turn, expected):
    with pytest.raises(expected):
        car = Car('test')
        car.turn(turn)


@pytest.mark.parametrize('speed, expected', [
    (50, '"test" have current speed 50 km/h'), (0, '"test" have current speed 0 km/h')])
def test_car_show_speed(monkeypatch, speed, expected):
    out_print = []
    monkeypatch.setattr('builtins.print', lambda *args: out_print.extend(map(str, args)))
    c = Car('test', speed=speed)
    c.show_speed()
    assert ''.join(out_print) == expected


@pytest.mark.parametrize('speed, expected', [
    (0, '"test" have current speed 0 km/h'),
    (60, '"test" have current speed 60 km/h'),
    (61, '"test" have current speed 61 km/h\n!!!Speed limit!!!')])
def test_town_car_speed_limit(monkeypatch, speed, expected):
    out_print = []
    monkeypatch.setattr('builtins.print', lambda *args: out_print.extend(map(str, args)))
    t = TownCar('test', speed=speed)
    t.show_speed()
    assert '\n'.join(out_print) == expected


@pytest.mark.parametrize('speed, expected', [
    (0, '"test" have current speed 0 km/h'),
    (40, '"test" have current speed 40 km/h'),
    (41, '"test" have current speed 41 km/h\n!!!Speed limit!!!')])
def test_work_car_speed_limit(monkeypatch, speed, expected):
    out_print = []
    monkeypatch.setattr('builtins.print', lambda *args: out_print.extend(map(str, args)))
    w = WorkCar('test', speed=speed)
    w.show_speed()
    assert '\n'.join(out_print) == expected
