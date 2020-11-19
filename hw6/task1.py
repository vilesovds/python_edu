# -*- coding: utf-8 -*-
from time import sleep
from itertools import cycle


class TrafficLight:
    __colors = ('red', 'yellow', 'green')
    __default_timers = {'red': 7, 'yellow': 2, 'green': 5}

    def __init__(self, **kwargs):
        """"""
        self.__times = TrafficLight.__default_timers.copy()
        self.apply_times(**kwargs)
        self.__color = cycle(TrafficLight.__colors)

    def get_colors(self):
        return TrafficLight.__colors

    def set_default_timers(self):
        self.__times = TrafficLight.__default_timers.copy()

    def apply_times(self, **kwargs):
        for k, v in kwargs.items():
            if k in self.__times.keys():
                if v <= 0:
                    raise ValueError("Unsupported value for time")
                self.__times[k] = v

    def running(self):
        for light in self.__color:
            t = self.__times[light]
            print(f'{light} will be on for {t} sec(s)')
            for s in range(t, 0, -1):
                print(f'{s}')
                sleep(1)


if __name__ == '__main__':
    tl = TrafficLight(red=4, yesllow=2, green=5)
    tl.running()
