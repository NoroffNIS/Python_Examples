def fibonacci_gen():
    a = b = 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci_gen()

for i in fib:
    if i > 100:
        break
    else:
        print('Generated: ', i)

print(next(fib))

