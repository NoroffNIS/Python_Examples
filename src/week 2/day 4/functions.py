def add():
    number_1 = 1
    number_2 = 2
    print('This will add together number ', number_1, 'and ', number_2)
    sum = number_1 + number_2
    print('The sum is: ', sum)

def main():
    print('Main function')
    function_name()
    print('After function')

def function_name():
    print('Inside function\n'*10, end='')

if __name__ == '__main__':
    main()

