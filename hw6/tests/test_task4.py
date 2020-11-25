# -*- coding: utf-8 -*-
import pytest
from task4 import WordSide


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
