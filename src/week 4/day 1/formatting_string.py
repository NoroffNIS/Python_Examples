import math
# var1 = 'Pølse'
# string = '{1} and {0}'.format(var1, 'Brød')
# print(string)
#
# string = '%s and %s' % ('Pølse', 'Brød')
#
# print(string)
#

pi = math.pi
string = '{:010.6}'.format(pi)
print(string)

string = '%010.5f' % (pi)
print(string)
