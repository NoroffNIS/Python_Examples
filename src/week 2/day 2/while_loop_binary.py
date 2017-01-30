count = 0
abbrertions = ''
while count < 41:
    size = byte = 2 ** count
    if byte < 1024:
        abbrertions = 'Byte'
    elif byte < 1048576:
        abbrertions = 'KB'
        size = byte / 1024
    elif byte < 1073741824:
        pass

    print('2^',count, ' - ', byte,' - ', size, abbrertions)
    count +=1