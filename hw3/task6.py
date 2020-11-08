def int_func(word: str):
    """
    takes a word from small Latin letters and returns it, but with an uppercase first letter
    :param word: small Latin letters string
    :return: string
    """
    upper_case_mask = 0xDF
    res = bytearray(word.encode())
    res[0] &= upper_case_mask
    return res.decode()


def custom_title(text: str):
    """
    every new word will start with capital later
    :param text: string
    :return: string
    """
    li = map(int_func, text.split())
    return ' '.join(li)


print(int_func('text'))
print(custom_title('some text with spaces'))
