title = '`Noroff Programming'
lotto = [1,2,3,4]
try:
    print(lotto[2])
except IndexError as msg:
    print(msg)
finally:
    print('Hope you win someday!')
value_input = ''
while value_input != 'Exit':
    value_input = input('Type in a number:')
    try:
        value_input = int(value_input)
    except ValueError as msg:
        print('Error! You have to type in a number.\n',msg)
        continue
    value_input = value_input ** value_input
    print(value_input)