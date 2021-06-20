import sys


def my_range(start: int, stop: int, step=1):
    print('The range has started')
    if start > stop:
        raise RuntimeError('Start should be less than end')
    i = start
    while i < stop:
        yield i
        print("The value of yield is {}".format(i))
        i += step


# trial_range = range(10)
trail_range = my_range(0, 10)
print("This is line 15")

trail_list = []

# print(next(trail_range))
# print(next(trail_range))

for index in trail_range:
    # print("{0}{0}".format(index))
    # print("Ya we have got it *****")
    trail_list.append(index)

trial_range2 = range(0, 10)

trial_list1 = []
for index in trial_range2:
    trial_list1.append(index)

print(trail_list)
print("*"*10)
print(trial_list1)
# print("The size of the list is {}b".format(sys.getsizeof(trail_list)))
# print("the size of the range is {}b".format(sys.getsizeof(trail_range)))


