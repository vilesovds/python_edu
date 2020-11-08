# solution # 1
def print_user_info(name, surname, birthday, city, email, phone):
    fstr = f'user info: name: "{name}", surname: "{surname}", birthday: "{birthday}", city: "{city}", ' \
           f'email: "{email}", phone: "{phone}"'

    print(fstr)


# # solution with args
def print_user_info_args(*args):
    print_user_info(*args)


# solution with kwargs
def print_user_info_kwargs(**kwargs):
    print_user_info(**kwargs)


print_user_info(phone='+79629747326', surname='Masterenko', name='Ivan', birthday='16.09.1985', city='Moscow',
                email='matser.i@mail.ru')

print_user_info('Ivan', 'Masterenko', '16.09.1985', 'Moscow', 'matser.i@mail.ru', '+79629747326')

print_user_info_args('Ivan', 'Masterenko', '16.09.1985', 'Moscow', 'matser.i@mail.ru', '+79629747326')

print_user_info_kwargs(surname='Masterenko', birthday='16.09.1985', city='Moscow',
                       email='matser.i@mail.ru', phone='+79629747326', name='Ivan')
