def my_func(x: int, y: int):
    """
    raising a number to a power
    :param x: base, int
    :param y: power, negative int
    :return:
    """
    return x**y


def my_func2(x: int, y: int):
    """
    raising a number to a power. Using loop
    :param x: base, int
    :param y: power, negative int
    :return: float
    """
    res = 1
    for _ in range(abs(y)):
        res *= x
    return 1 / res


assert(my_func(2, -3) == pow(2, -3))
assert(my_func2(2, -3) == pow(2, -3))
assert(my_func(-1, -1) == pow(-1, -1))
assert(my_func2(-1, -1) == pow(-1, -1))
