chars = ['Alpha', 'Beta', 'Gamma']


def display(elem):
    assert type(elem) is int, 'Argument Must Be Integer!'
    print('List Element', elem, '=', chars[elem])

elem = 2
print(type(elem))
display(elem)

elem /= 2
print(type(elem))
display(elem)

print('Program ended')
