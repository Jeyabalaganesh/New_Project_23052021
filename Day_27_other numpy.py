import numpy as np

# f = lambda m, n: m**2 + n**2
#
# a = np.fromfunction(f, (5, 3))
# print(a)
# print(np.identity(3, dtype=int))
# print(np.eye(5, dtype=int, k=2))
# print(np.eye(5, dtype=int, k=-2))
#
#
# print("*"*25)
#
# diagonal = np.arange(0,25,7)
# dia_array = np.diag(diagonal, k =0)
# print(dia_array)
# dia_array = np.diag(diagonal, k =-1)
# print(dia_array)
#
# print("*"*25)

x = np.arange(0, 13)
y = np.array([1, 8, 54, 21])
print(x)
print(y)
print("******")
X, Y = np.meshgrid(x, y)
print(X)
print("*"*25)
print(Y)
print(X**2 + Y**2)
print("*"*25)

b = np.ones_like(X)
print(b)

sub_b = b[1:4, 1:4].copy()
print(sub_b)
sub_b[:, :] = 0
print(sub_b)
print(b)

sub_b = b[1:4, 1:4]
print(sub_b)
sub_b[:, :] = 0
print(sub_b)
print(b)



