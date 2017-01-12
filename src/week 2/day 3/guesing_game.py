'''
Comments, Doc
'''

# comment

import random
random_number = random.randint(0, 100)
user_input = ''
print('print\n'
      'print 2')
print('''
hello
world
''')

while user_input != 'Give up':
    user_input = input('Guess what number I\'m thinking off.\nType in a number:')
    try:
        user_input = int(user_input)
        if user_input == random_number:
            print('You guessed correct!')
            break
        else:
            print('You guessed wrong!')
            if user_input < random_number:
                print('My number is higher')
            else:
                print('My number is lower')

    except ValueError as msg:
        print(msg)
        break
