import re

# Any Characters
# string = 'p2hon py2hon py2hon'
# pattern = re.compile('py..on')
# is_valid = pattern.finditer(string)
# for match in is_valid:
#     print(string, ' match ', pattern, ':', match)

# #First Character
# string = 'python'
# pattern = re.compile('^py')
# is_valid = pattern.match(string)
# print(string, ' match ', pattern, ':', is_valid)

#Final Character
# string = 'python'
# pattern = re.compile('....on$')
# is_valid = pattern.match(string)
# print(string, ' match ', pattern, ':', is_valid)

# #Zero or more repetitions
# string = 'p y python py2'
# pattern = re.compile('py*')
# is_valid = pattern.findall(string)
# print(string, ' match ', pattern, ':', is_valid)
#
# #One or more repetitions
# string = 'p ython'
# pattern = re.compile('py+')
# is_valid = pattern.findall(string)
# print(string, ' match ', pattern, ':', is_valid)
#
# #Zero or One repetitions
# string = 'p ython p'
# pattern = re.compile('py?')
# is_valid = pattern.findall(string)
# print(string, ' match ', pattern, ':', is_valid)

# #Multiple repetitions
# string = 'n000b n00b n0b'
# pattern = re.compile('0{2}')
# is_valid = pattern.findall(string)
# print(string, ' match ', pattern, ':', is_valid)

# #Character class
# string = 'p1ytt1hon'
# pattern = re.compile('[a-z]+[0-9]+[a-z]')
# is_valid = pattern.findall(string)
# print(string, ' match ', pattern, ':', is_valid)

#Character class
string = 'p7'
pattern = re.compile('^(?=.*\d)(?=.*[a-zA-Z])[a-zA-Z\d]{0,8}$')
is_valid = pattern.fullmatch(string)
print(string, ' match ', pattern, ':', is_valid)

if is_valid:
    print(True)
else:
    print(False)

# #Special Sequence
# string = ' p1yt1hon'
# pattern = re.compile('\s')
# is_valid = pattern.match(string)
# print(string, ' match ', pattern, ':', is_valid)
#
# #Either Optional Character
# string = 'p1yt1hon'
# pattern = re.compile('([a-z]|[0-9])+[a-z]')
# is_valid = pattern.match(string)
# print(string, ' match ', pattern, ':', is_valid)
#
# #Expression Group
# string = 'P1y@t1hon'
# pattern = re.compile('([A-z]+[0-9]+[a-z])+(\W)')
# is_valid = pattern.findall(string)
# print(string, ' match ', pattern, ':', is_valid)
