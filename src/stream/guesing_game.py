import random


def human_guess():
    random_number = random.randint(0, 100)
    print('Rand:', random_number)

    user_input = ''
    while user_input != 'Exit':
        user_input = input('Type in the number:')
        try:
            if int(user_input) == random_number:
                print('Correct! You won!')
                break
            else:
                print('You guessed wrong!\nTry again.')
                if int(user_input) < random_number:
                    print('You need to guess higher!')
                elif int(user_input) > random_number:
                    print('You need to guess lower!')
                else:
                    print('Something went wrong!')
        except ValueError as msg:
            print('Bye Bye!')


def computer_guess():
    user_input = input('Type in the number:')
    not_correct = True
    low = 0
    high = 100

    while not_correct:
        random_number = random.randint(low, high)
        print('Rand:', random_number)

        if int(user_input) == random_number:
            print('Correct! Computer won!')
            not_correct = False
            break
        else:
            print('Computer guessed wrong!\nTry again.H:', high,'L:', low)
            if int(user_input) < random_number:
                high = random_number - 1
                print('You need to guess lower!')
            elif int(user_input) > random_number:
                low = random_number + 1
                print('You need to guess higher!')
            else:
                print('Something went wrong!')

user_input = ''

while user_input != 'Exit':
    user_input = input('Welcom to the guessing game!\n'
          'Type 1 for Human against computer\n'
          'Type 2 for computer against human:')

    if user_input == '1':
        human_guess()
    elif user_input == '2':
        computer_guess()
    else:
        print('You typed not a valid number!')

print('Bye Bye!')