
def add_line_to_list(path):
    file = open(path, "r")
    line_list = []
    for line in file:
        line_list.append(line)
    file.close()
    return line_list

file_1_list = add_line_to_list('Lorem_ipsum_1.txt')
file_2_list = add_line_to_list('Lorem_ipsum_1.txt')

maxlen = len(file_1_list) if len(file_1_list) >= len(file_2_list) else len(file_2_list)
minlen = len(file_1_list) if len(file_1_list) <= len(file_2_list) else len(file_2_list)

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

