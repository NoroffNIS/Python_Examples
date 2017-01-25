from People import *

people = People('Brage', 'Roalkvam')
print(people.name)

print('--Build-in instance attributes')
for attri in dir(people):
    if attri[0] == '_':
        print(attri)

for item in people.__dict__:
    print(item, ':', People.__dict__[item])