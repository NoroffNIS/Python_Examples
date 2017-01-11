def add(number_1=0, number_2=0):
    print('This will add together number ', number_1, 'and ', number_2)
    sum = number_1 + number_2
    print('The sum is: ', sum)

add(4, 4)

def display_welcome(name='user-name'):
    print('Welcome', name)

display_welcome()
user_name = input('Type in your name:')
display_welcome(user_name)

