# first part
str_var = 'String example'
int_var = -43
float_var = 1.3e+2
bool_var = bool()
# additional types
list_var = [1, 2, 3]
tuple_var = ('1', 2, print)
dict_var = {'name': 'Boris', 'age': 20}

print('str_var:\n\ttype:', type(str_var), '\n\tvalue:', str_var)
print('int_var:\n\ttype:', type(int_var), '\n\tvalue:', int_var)
print('float_var:\n\ttype:', type(float_var), '\n\tvalue:', float_var)
print('bool_var:\n\ttype:', type(bool_var), '\n\tvalue:', bool_var)

print('list_var:\n\ttype:', type(list_var), '\n\tvalue:', list_var)
print('tuple_var:\n\ttype:', type(tuple_var), '\n\tvalue:', tuple_var)
print('dict_var:\n\ttype:', type(dict_var), '\n\tvalue:', dict_var)
print('-' * 40)

user_int_var = int(input('Type some number and press Enter: '))
user_int_var2 = int(input('Type some number and press Enter: '))
print('Your numbers are:', user_int_var, user_int_var2)

user_str_var = input('Type some string and press Enter: ')
user_str_var2 = input('Type some string and press Enter: ')
print('Your strings are: "', user_str_var, '" ', '"', user_str_var2, '"', sep='')

# second part
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60

seconds = int(input('Please enter time in seconds: '))
hours = seconds // SECONDS_IN_HOUR
seconds %= SECONDS_IN_HOUR
minutes = seconds // SECONDS_IN_MINUTE
# last part - just seconds
seconds %= SECONDS_IN_MINUTE
# and result
print(f'{hours:02}:{minutes:02}:{seconds:02}')

# third part
digit = input('Please enter some number: ')
single_number = int(digit)
double_number = int(digit * 2)
triple_number = int(digit * 3)

result = single_number+double_number+triple_number
print(f'Sum {single_number}+{double_number}+{triple_number} is:', result)

# fourth part
# decimal base
BASE = 10
user_number = int(input('Please enter some positive number: '))
maximum = 0
while user_number:
    digit = user_number % BASE
    # print(number)
    if digit > maximum:
        maximum = digit
    user_number //= BASE
print('Maximum digit is:', maximum)

# fifth part
income = int(input('Please inter income: '))
outgoings = int(input('Please inter outgoings: '))

profit = income - outgoings
if profit < 0:
    print(f'You works with loss {abs(profit)}')
elif profit == 0:
    print('You works without loss and profit')
else:
    print(f'You works with profit {profit}')
    profitability = profit/income
    print('Your ROI is:', profitability)
    employees_number = int(input('Enter the number of company employees: '))
    print('Profit of the company per employee:', profit/employees_number)
