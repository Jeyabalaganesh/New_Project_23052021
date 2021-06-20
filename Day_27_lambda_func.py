def square_sums(x, y):
    return x**2 + y**2


print(square_sums(1.5, 5.7))
"""
ananymous function: Lambda function
syntax: lambda argument: expression 
"""
f = lambda a, b: a**2 + b**2 if (a > b) else (a**3 + b**3)


print(f(1.5, 5.7))
print(type(f))
max = lambda a, b, c, d: a if ((a > b) & (a > c) & (a > d)) else (b if ((b > a) & (b > c) & (b > d)) else (c if ((c > a) & (c > b) & (c > d)) else d))

print(max(9, 1, 5, 4))
print(max(9, 11, 5, 4))
print(max(9, 1, 52.3, 4))
print(max(9, 1, 5, 47.245))