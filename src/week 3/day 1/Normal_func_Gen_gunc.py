def normal_fun():
    i = 0
    while True:
        i += 1
        if i< 100:
            return i
        else:
            break

def gen_fun():
    i = 0
    while True:
        yield i
        i += 1

gen = gen_fun()
nor = normal_fun()

print(nor)
print(nor)