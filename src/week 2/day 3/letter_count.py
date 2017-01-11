word = input('Type in a word:').upper()
letter = input('Type in a letter you want to count:').upper()
count = 0

for l in word:
    if l == letter:
        count += 1
    else:
        pass
print('In you word', word, 'there is', count, 'letters of', letter)