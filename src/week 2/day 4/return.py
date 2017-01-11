def add(number_1=0, number_2=0):
    print('This will add together number ', number_1, 'and ', number_2)
    sum = number_1 + number_2
    print('The sum is inside the function: ', sum)
    return sum


sum1 = add(4, 4)
print('Sum outside function is: ', sum1)


def display_welcome(name='user-name'):
    return 'Welcome '+ name

return_string = display_welcome()
print(type(return_string))
print(return_string)
user_name = input('Type in your name:')
print(display_welcome(user_name))