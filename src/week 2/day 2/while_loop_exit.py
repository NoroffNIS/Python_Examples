what_to_do = ''
while what_to_do != 'Exit':
    what_to_do = input('Type in Exit to quit, '
                       'or something else to continue: ')
    if what_to_do == 'Exit':
        print('You typed in Exit, program stopped')
    elif what_to_do == 'exit':
        print('You typed in Exit, loop break, program stopped')
        break
    else:
        pass

print('Out of loop!')