def odd_gen():
    num = 1
    while True:
        yield num
        num += 2

def est_pi():
    nxt_odd_num = odd_gen()
    pi = 0
    while True:
        pi += 4/next(nxt_odd_num)
        yield pi
        pi -= 4/next(nxt_odd_num)
        yield pi

pi_val = est_pi()

for index in range(100):
    print(next(pi_val))