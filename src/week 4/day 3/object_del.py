from People import *

people = People('Brage', 'Roalkvam')
print(people.name, 'ID:', id(people))
people_1 = People('Gunnar', 'Salvesen')
print(people_1.name, 'ID:', id(people_1))
people_2 = People('Tom', 'Drange')
print(people_2.name, 'ID:', id(people_2))
input()
del(people)
input()
del(people_2)
del(people_1)
input()

