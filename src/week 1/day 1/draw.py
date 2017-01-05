print('   /\ ')
print('  /  \\')
print(' /    \\')
print('/______\\')
print('|      |')
print('|      |')
print('|      |')
print('|______|')

house = {  'roof_1':'   /\ ',
           'roof_2':'  /  \\',
           'roof_3':' /    \\',
           'roof_4':'/      \\',
           'wall':'|      |',
           'base_1':'|------|',
           'base_2':'|______|'}

print(house['roof_1'], house['roof_2'], house['roof_3'],house['roof_4'],
      house['base_1'], house['wall'], house['wall'],house['wall'],
      house['base_2'],sep='\n')