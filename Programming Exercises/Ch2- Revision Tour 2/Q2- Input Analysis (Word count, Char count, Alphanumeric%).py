print('Enter Input to be analysed'.title())

input_str = input('>>')

word_count = len(input_str[:].split(' '))

char_count = len(input_str)

alpha_numeric_count = sum(i.isalnum() for i in input_str)

alpha_numeric_percentage = round((alpha_numeric_count/char_count)*100, 2)

print('-'*15 + 'Report on Input' + '-'*15)
print('Given Input    :', input_str)
print('Word Count     :', word_count)
print('Charecter Count:', char_count)
print('Alpha-Numeric %:', str(alpha_numeric_percentage) + '%')
print('-'*15 + 'End of Report' + '-'*17)

exit_var = input('Enter Any Input To Exit')