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
