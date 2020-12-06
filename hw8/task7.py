# -*- coding: utf-8 -*-
"""
Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, real_part, imaginary_part):
        self.real = real_part
        self.img = imaginary_part

    def __str__(self):
        return f"{self.real}{self.img:+}j"

    def __repr__(self):
        return f"({self.real}{self.img:+}j)"

    @staticmethod
    def _validate(some):
        if not type(some) is ComplexNumber:
            raise TypeError(f'Only ComplexNumber type supported, but got {type(some)}')

    def __add__(self, other):
        self._validate(other)
        return ComplexNumber(self.real + other.real, self.img + other.img)

    def __mul__(self, other):
        self._validate(other)
        a, b, c, d = self.real, self.img, other.real, other.img
        return ComplexNumber(a*c - b*d, b*c + a*d)


if __name__ == '__main__':
    num1 = ComplexNumber(3, 0)
    print(num1)
    num2 = ComplexNumber(-4, -3)
    print(num2)
    num3 = ComplexNumber(1, 5)
    print(num3)
    print([num1, num2, num3])

    num_sum = num1 + num2 + num3
    print('num_sum', num_sum)
    expected = complex(3, 0) + complex(-4, -3) + complex(1, 5)
    print('expected', expected)
    assert num_sum.real == expected.real
    assert num_sum.img == expected.imag

    num_mul = num1 * num2 * num3
    print('num_mul', num_mul)
    expected = complex(3, 0) * complex(-4, -3) * complex(1, 5)
    print('expected', expected)
    assert num_mul.real == expected.real
    assert num_mul.img == expected.imag

    wrong_num = 'text'
    num1 * wrong_num
