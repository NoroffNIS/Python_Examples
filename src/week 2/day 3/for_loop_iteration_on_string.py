word = input('Type in a word')
print(word)

print(word[0], word[1], word[2])

count = 0
for letters in word:
    count += 1
    #print(letters, end='')
    print(count, 'BOKSTAV ER:', letters)