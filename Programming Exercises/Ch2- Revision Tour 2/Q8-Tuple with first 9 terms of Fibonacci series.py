output = (0,1)

for i in range(2,2+7):
    new_term = output[i-2]+output[i-1]
    output = output + (new_term,)
    
print(output)

exit_var = input('Enter Any Input To Exit')