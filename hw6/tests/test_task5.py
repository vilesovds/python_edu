# -*- coding: utf-8 -*-
from task5 import Stationery


def test_stationery_title():
    assert Stationery().title == 'Stationery'


def test_stationery_draw(monkeypatch):
    out_print = []
    monkeypatch.setattr('builtins.print', lambda *args: out_print.extend(map(str, args)))
    s = Stationery()
    s.draw()
    assert ''.join(out_print) == 'Запуск отрисовки'
