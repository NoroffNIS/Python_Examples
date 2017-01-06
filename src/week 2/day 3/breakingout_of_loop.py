for number in range(100):
    if number % 10 == 0:
        print('This number is 10s')
        continue
    if number % 2 == 0:
        print(number, ' is even number')
    if number == 52:
        print('This number is 52:', number)
        break
    else:
        pass
