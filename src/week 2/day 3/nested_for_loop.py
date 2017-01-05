
for i in range(1, 11):
    print(' ')
    for j in range(0, i):
        print(str(j), end='')
print('\n-------------------\n')

for i in range(10, -1, -1):
    print(' ')
    for j in range(0, i):
        print(str(j), end='')
print('\n-------------------\n')

for i in range(0, 10):
    print(' ')
    for j in range(0, i):
        print(str(' '), end='')
    for k in range(0, 10-i):
        print(str(k), end='')
print('\n-------------------\n')

for i in range(9, -1, -1):
    print()
    for j in range(0, i):
        print(str(' '), end='')
    for k in range(0, 10-i):
        print(str(k), end='')
print('\n-------------------\n')