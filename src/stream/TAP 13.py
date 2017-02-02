import math

a = 23
b = 23

c = math.sqrt(math.pow(a,2) + math.pow(b,2))
print('A:',a, 'B',b, 'C:',c)

v_c = 90
v_a = math.asin(b/c)
v_b = math.acos(b/c)
print('vA:',v_a, 'vB',v_b, 'vC:',v_c)
v_a = math.degrees(v_a)
v_b = math.degrees(v_b)
print('vA:',v_a, 'vB',v_b, 'vC:',v_c)