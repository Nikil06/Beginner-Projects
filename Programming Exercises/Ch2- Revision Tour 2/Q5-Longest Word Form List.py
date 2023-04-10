words = ["apple", "banana", "cherry", "date"]

longest_word = ''

for i in words:
    if len(i) > len(longest_word):
        longest_word = i

print('Words:- ', end = '')
[print(i, end = ' ') for i in words]
print('\n')

print('Longest Word:', longest_word)

exit_var = input('Enter Any Input To Exit')