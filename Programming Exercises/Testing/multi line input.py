lines = []
while True:
    line = input('>>')
    if not line:
        break
    lines.append(line)
multiline_input = '\n'.join(lines)

try:
    exec(multiline_input)
except Exception as e:
    print('ERROR: {}'.format(e))

input('Enter any input to quit: ')


lines = []
while True:
    line = input('>>')
    if not line:
        break
    lines.append(line)
multiline_input = '\n'.join(lines)

try :
    exec(multiline_input)
except:
    print('ERORR '*10)

input('Enter any input to quit: ')
