str_1 = 'Jimmy'
str_2 = 'Johny'

str_1, str_2 = str_2[:], str_1[:]

print(str_1)
print(str_2)

'''
If this is confusing, this is called tuple packing and unpacking method,

in line 4  we create a tuple that contains the values of
the two variables we want to swap, and then we unpack the
tuple into the variables in reverse order.
'''

exit_var = input('Enter Any Input To Exit')