# -*- coding: utf-8 -*-
"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
"""
from dataclasses import dataclass


# class decorator definition
def class_attributes(default_attr, more_allowed_attr):
    def class_decorator(cls):
        def args_init(self, *args, **kwargs):
            allowed_attr = list(default_attr.keys()) + more_allowed_attr
            default_attr.update(kwargs)
            self.__dict__.update((k, v) for k, v in default_attr.items() if k in allowed_attr)

        cls.__init__ = args_init
        return cls

    return class_decorator


class Car:
    """
    Base Car storage
    """
    speed = 0
    color = 'black'
    name = 'some car'
    is_police = False

    def go(self, speed):
        self.speed = speed
        """
        """
        print('Car started')

    def stop(self):
        self.speed = 0
        print('Car stopped')

    def turn(self, direction):
        print(f'Car turned to the {direction}')

    def show_speed(self):
        print(f'current speed {self.speed} km/h')


# @class_attributes(dict(name='Town car'), ['color', 'is_police'])
class TownCar(Car):
    __speed_limit = 60

    def __init__(self, name, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.name = name

    def show_speed(self):
        super().show_speed()
        if self.speed > self.__speed_limit:
            print(f'!!!Speed limit!!!')


if __name__ == '__main__':
    tc = TownCar('Kia Rio', color='yellow')
    print(tc.__dict__)
    tc.go(40)
    tc.show_speed()
    tc.turn('left')
    tc.show_speed()
    tc.go(90)
    tc.show_speed()
