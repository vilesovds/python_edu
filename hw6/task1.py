# -*- coding: utf-8 -*-
# import time
from time import sleep
from itertools import cycle


class TrafficLight:
    __colors = ('red', 'yellow', 'green')
    __default_timers = {'red': 7, 'yellow': 2, 'green': 5}


    def __init__(self, **kwargs):
        self.__times = TrafficLight.__default_timers.copy()
        self.apply_times(**kwargs)
        self.__color = cycle(TrafficLight.__colors)

    @staticmethod
    def get_colors():
        return TrafficLight.__colors

    def set_default_timers(self):
        self.__times = TrafficLight.__default_timers.copy()

    def apply_times(self, **kwargs):
        for k, v in kwargs.items():
            if k not in self.__times.keys():
                raise KeyError(f"Params should be one of this: {', '.join(self.__times.keys())}")
            v = int(v)
            if v <= 0:
                raise ValueError("Unsupported value for time")
            self.__times[k] = v

    def running(self):
        while True:
            light = next(self.__color)
            t = self.__times[light]
            print(f'{light} will be on for {t} sec(s)')
            for s in range(t, 0, -1):
                print(int(s))
                sleep(1)


if __name__ == '__main__':
    tl = TrafficLight(green=5)
    tl.running()
