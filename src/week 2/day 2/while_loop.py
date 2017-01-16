count = 0

while count <= 10:
    print('Count:', count, ' - ', 2 ** count)
    count += 1

num = 1
print(num)
while True:
    num *= 2
    if num > 1000:
        break
    print(num)