dict = {'name':'Bob', 'number':'99999999'}
print('dict:', dict)
print(dict['number'])
dict['number'] = 00000000
print('dict:', dict)
del dict['name']
print('dict:', dict)
dict['name'] = 'Tom'
print('dict:', dict)
dict['name'] = 'Ola'
print('dict:', dict)

print(dict.keys())
print(dict.values())
boolean = 'name' in dict
print('Key "name" is in dict: ', boolean)