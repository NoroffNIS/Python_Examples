import math

side_a = 0
side_b = 0
side_c = 0

angel_x = 90
angel_y = 0
angel_z = 0

side_a = int(input('Enter length of side A:'))
side_b = int(input('Enter length of side B:'))
side_c = math.sqrt(math.pow(side_a,2) + math.pow(side_b, 2))

angel_y = math.degrees(math.asin(side_b/side_c))
angel_z = math.degrees(math.acos(side_b/side_c))

print('Side A = ', side_a)
print('Side B = ', side_b)
print('Side C = ', side_c)

print('Angel x = ', angel_x)
print('Angle y = ', angel_y)
print('Angel z = ', angel_z)

