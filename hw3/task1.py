# simple way

def simple_div(a, b):
    """
    division procedure
    :param a: dividend number
    :param b: divisor number
    :return: division result or None
    """
    if b != 0:
        return a/b
    else:
        return float('nan')


# decorator way

def anti_zero_div_exception(fn):
    def core_func(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except ZeroDivisionError:
            return float('nan')
    return core_func


@anti_zero_div_exception
def vars_division(a, b):
    """
    simple division a/b
    :param a: dividend number
    :param b: divisor number
    :return: division result
    """
    return a/b


number1 = float(input('Please inter number a: '))
number2 = float(input('Please inter number b: '))
print('Result simple_div   : ', simple_div(number1, number2))
print('Result vars_division: ', vars_division(number1, number2))
