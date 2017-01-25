from People import *

people = People('Brage')
people.age = 20
print('numeber of people:', people.count)
people.display_name()
people.display_age()
print('-----')
people_1 = People('Gunnar')
people_1.age = 30
people_1.display_name()
people_1.display_age()
print('numeber of people:', people.count)

print('1:',hasattr(people, 'age'))
print('2:',getattr(people, 'name'))
print('3:',setattr(people, 'age', 40))
print('4:',getattr(people, 'age'))
print('5:',delattr(people, 'age'))
print('6:',getattr(people, 'age'))
print('7:',hasattr(people, 'address'))

