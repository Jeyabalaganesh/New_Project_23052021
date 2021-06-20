# Fibonacci Series

def fiboonacci_gen():
    current, previous = 0, 1
    while True:
        yield current
        current, previous = current + previous, current

fib = fiboonacci_gen()

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))

