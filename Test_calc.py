import math
p = 0.0128
n = 200
Sum = 0

for i in range(9):

    result = math.comb(n,i) * math.pow(p,i) * math.pow((1-p), (n-i))
    Sum += result


print("{:.4f}".format(Sum))
