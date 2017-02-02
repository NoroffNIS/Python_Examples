min = 0
max = 10

print('-----1-----')
for x in range(min, max):
    for y in range(min, x):
        print('*', end='')
    print('')

print('-----2-----')

for x in range(max, min, -1):
    for y in range(min, x):
        print('*', end='')
    print('')

print('-----3-----')

for x in range(min, max):
    for y in range(min, x):
        print(' ', end='')
    for y in range(max, x, -1):
        print('*', end='')
    print('')

print('-----4-----')

for x in range(max, min, -1):
    for y in range(min, x):
        print(' ', end='')
    for y in range(max, x, -1):
        print('*', end='')
    print('')

print('-----4-----')

for x in range(max, min, -1):
    for y in range(min, x):
        print(' ', end='')
    for y in range(max, x, -1):
        print('*', end='')
    print('')