print('Buss ticket price.')
user_age = input('Type in you age!')
user_age = int(user_age)

if user_age <=4:
    print('Your ticket is free!')
elif user_age <= 16:
    print('You have a child ticket!')
elif user_age <= 20:
    print('You have a youth ticket!')
elif user_age <= 80:
    print('You have an adult ticket!')
else:
    print('You have an bike ticket!')

