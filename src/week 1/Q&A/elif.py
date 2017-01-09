temp = input('Type in the temperature')

if temp <= 0:
    print('Its freezing!')
elif temp <= 4:
    print('It\'s cold')
elif temp <= 10:
    print('It\'s getting better')
elif temp <= 15:
    print('It\'s good')
else:
    print('It\'s hot')
