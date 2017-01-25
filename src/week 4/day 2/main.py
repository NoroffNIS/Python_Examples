file_1_list = []
file_2_list = []

file_1 = open("Lorem_ipsum_3.txt", "r")
file_2 = open("Lorem_ipsum_1.txt", "r")

print(file_1.__sizeof__())
print(file_2.__sizeof__())

for line in file_1:
    file_1_list.append(line)

for line in file_2:
    file_2_list.append(line)

maxlen = len(file_1_list) if len(file_1_list) > len(file_2_list) else len(file_2_list)
minlen = len(file_1_list) if len(file_1_list) < len(file_2_list) else len(file_2_list)

total = 0
equal = 0

print(minlen, '-', maxlen)

for l in range(0, maxlen):
    if total < minlen:
        if file_1_list[l] == file_2_list[l]:
                equal += 1
        total += 1
    else:
        total += 1

print('Equal:', equal, 'Total:', total)
print('Equal:', (equal/total)*100, '%')

