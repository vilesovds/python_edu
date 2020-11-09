def my_func(*args):
    """
    takes three positional arguments, and returns the sum of the largest two arguments
    :param args: some numbers
    :return: float
    """
    if len(args) < 2:
        raise Exception('Wrong count of arguments. Should be >= 2')

    li = list(args)
    li.sort(reverse=True)
    return li[0] + li[1]


assert(my_func(1, 2, 4) == 6)
assert(my_func(7.2, -1.5, 2.5, 6, 8.5) == 15.7)

assert(my_func(1, 2) == 3)
assert (my_func(*(x for x in range(100))) == 197)
