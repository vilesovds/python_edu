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
