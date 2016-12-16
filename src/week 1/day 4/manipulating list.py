my_list = [1,2,3,4,5,7,8]
print(my_list)
my_list.append(9)
print(my_list)
my_list2 = [10,11,12,13,14,15,17,18]
my_list.extend(my_list2)
print(my_list)
print(my_list.pop(4))
print(my_list)
my_list.remove(15)
print(my_list)
my_list.insert(13,12)
print(my_list)
print(my_list.count(12))
print(my_list.index(12))
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)

my_set = {'Red', 'Blue', 'Green'}
my_set.add('Yellow')
my_set.discard('Blue')
print(my_set)
my_set2 = {'Blue', 'Red'}
print(my_set.difference(my_set2))
print(my_set.intersection(my_set2))