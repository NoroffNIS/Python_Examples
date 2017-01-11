title = 'Programming at Noroff'
try:
    print(titel)
except NameError as msg:
    print(msg)

day = 34
try:
    if day < 32:
        print('Day is ', day)
    else:
        raise ValueError('Invalid day number')
except (ValueError, NameError) as msg:
    print(msg)
finally:
    print('A beautiful day anyway!')
