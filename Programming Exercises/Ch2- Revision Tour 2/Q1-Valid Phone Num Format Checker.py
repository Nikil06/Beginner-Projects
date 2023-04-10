'''Phone Number Format Checker'''
'''first here we have my solution which came to me first then we have a commented code
which uses the re module ie. regular expressions to help us dot it a lot more efficiently for large ammounts of data to be checked -ChatGPT Solution'''

digit_char = '0'; dashes_char = '-'
valid_format = digit_char*3 + dashes_char + digit_char*3 + dashes_char + digit_char*4

input_num = input('Enter Number to be checked:- ')

def check_num(num: str)-> bool:
    if len(num) != len(valid_format):
        return False
    for i in range(len(valid_format)):
        if valid_format[i] == digit_char:
            if not num[i].isdigit():
                return False
        elif valid_format[i] == dashes_char:
            if num[i] != '-':
                return False
    return True

if check_num(input_num):
    print(input_num, 'is a valid input.')
else:
    print(input_num, 'is an invalid input')

exit_var = input('Enter Any Input To Exit')


'''
import re

phone_pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')

input_num = input('Enter Number to be checked:- ')

if phone_pattern.match(input_num):
    print(input_num, 'is a valid input.')
else:
    print(input_num, 'is an invalid input.')

'''
