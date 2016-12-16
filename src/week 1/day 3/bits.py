a = 2
b = 2
print('a:',a, '\tb:', b)

print("a:\t{0:04b}".format(a), '\n', "b:\t{0:04b}".format(b), sep='')

c = a << b
print("c:\t{0:04b}".format(c))

print('c:', c)