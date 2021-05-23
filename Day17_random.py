import random
import time
import statistics as ss

start_time = time.time()

for i in range(10):
    a =random.randrange(1,15,2)
    print(a)

end_time =time.time()

print("{:.10f}".format(end_time - start_time))


c= random.getrandbits(5)
print(c)


l =list(range(100))
# print(l)
random.shuffle(l)
print(l)

l_r = random.choice(l)
print(l_r)

sam = random.sample(l,5)
print(sam)
print(random.random())  ## Return the next floating poing value in the range 0,1
print(random.uniform(0,10.5))  ## Return the next floating poing value in the range 0,10.5
print(random.triangular(0,10.5,2)) ## Return the next floating poing value in the range 0,10.5 but with mode 2

# l2 = list(range(10,58,2))
# print(statistics.mean(l2))
# print(statistics.fmean(l2))
# print(statistics.geometric_mean(l2))
# print(statistics.harmonic_mean(l2))
l3 = [4,7.5, 92.34, 21.9]
# print(statistics.median(l3))
# print(statistics.median_low(l3))
# print(statistics.median_high(l3))

print (ss.mean(l3))

