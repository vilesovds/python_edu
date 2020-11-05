# part 1
example_list = ['str', 98, 1.3e-2, {1, 2, 3}, False, f'f-string', print, (1 + 3j), [chr(8), 9, 1, 1], None, reversed]
for el in example_list:
    print('element: ', el, '\ntype: ', type(el))
    print('')


# part 2
print('-'*40)

s_list = []
while True:
    s = input('Please inter something: ')
    if s == '':
        break
    s_list.append(s)

print('list before: ', s_list)

for i in range(0, len(s_list) - 1, 2):
    s_list[i], s_list[i + 1] = s_list[i + 1], s_list[i]

print('list  after: ', s_list)


# I found another way by slices
print('-'*40)

s_list = []
while True:
    s = input('Please inter something: ')
    if s == '':
        break
    s_list.append(s)

print('list before: ', s_list)

if len(s_list) > 1:
    rounded_length = (len(s_list) + 1) // 2
    s_list[:rounded_length:2], s_list[1::2] = s_list[1::2], s_list[:rounded_length:2]

print('list  after: ', s_list)


# part 3
print('-'*40)

SEASONS_LIST = ('Winter', 'Winter',
                'Spring', 'Spring', 'Spring',
                'Summer', 'Summer', 'Summer',
                'Fall', 'Fall', 'Fall',
                'Winter')

SEASONS_DICT = {str(k): v for (k, v) in enumerate(SEASONS_LIST, 1)}

month_str = input('Enter the month as an integer from 1 to 12: ')
# list solution
month = int(month_str)
if month in range(1, 13):
    print(SEASONS_LIST[month-1])
else:
    print('Error: Wrong number')

# dict solution. Quite short ))
print(SEASONS_DICT.get(month_str) or "Season not found")


# part 4
print('-'*40)

user_str = input('Please enter some string: ')

for n, s in enumerate(user_str.split(), 1):
    print(f'{n}: "{s[:10]}"')


# part 5
print('-'*40)


def colored_print(li: list, colored: int):
    """ colored output like in training manual. Used ANSI colors in terminal """
    li_length = len(li)
    for num, v in enumerate(li):
        if num == colored:
            print(f"\u001b[31m{v}\u001b[0m", end='')
        else:
            print(v, end='')
        if num != li_length-1:
            print(',', end=' ')
        else:
            print('.')


# solution by iteration only
s_list = [7, 5, 3, 3, 2]
while True:
    in_str = input('Enter new number: ')
    if in_str == '':
        break

    new_v = int(in_str)
    idx = 0
    for i, v in enumerate(s_list):
        if new_v > v:
            break
        idx = i + 1

    s_list.insert(idx, new_v)
    colored_print(s_list, idx)

# another way by count and index. I think it's complicated
print('-'*40)

s_list = [7, 5, 3, 3, 2]
while True:
    in_str = input('Enter new number: ')
    if in_str == '':
        break

    new_v = int(in_str)

    length = len(s_list)
    count = s_list.count(new_v)
    if count:
        idx = s_list.index(new_v) + count
    else:
        idx = 0
        for i, v in enumerate(s_list):
            if new_v > v:
                break
            idx = i + 1

    s_list.insert(idx, new_v)
    colored_print(s_list, idx)

# part 6
print('-'*40)

goods = []
while True:
    answer = input('Do you want add new item? Enter "yes" to continue: ')
    if answer.lower() != 'yes':
        break
    name = input('Enter name: ')
    price = float(input('Enter price: '))
    count = int(input('Enter count: '))
    unit = input('Enter unit: ')
    goods.append((len(goods), {'name': name, 'price': price, 'count': count, 'unit': unit}))

analytics = dict()
for _, item in goods:
    for k, v in item.items():
        vl = analytics.get(k) or []
        if v not in vl:
            vl.append(v)
        analytics[k] = vl

print('goods: ', goods)
print('analytics: ', analytics)
