import cmath

x = 4.10 + 3.02j
y = 5.1 + 2.7j
print(x-y)
a = complex(2,3.5)
print(a)
print((x+y).real)
print((x*y).imag)

print(cmath.phase(a))
b = cmath.polar(a)
r,theta = b
rect = cmath.rect(r,theta)
print(rect)



