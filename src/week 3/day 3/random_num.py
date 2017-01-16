import random

lotto = []
for i in range(0, 6):
    random_number = random.randint(0, 100)
    lotto.append(random_number)

print(lotto)

lotto_2 = random.sample(range(0, 100), 6)
print(lotto_2)
