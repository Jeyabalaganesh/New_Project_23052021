ages = [2, 45, 29, 97, 10, 5, 47, 33, 61, 13, 7]


def filter_condition(k):
    return k > 45


print(filter_condition(54), filter_condition(13))
filtered_list = list(filter(lambda age: age >= 45, ages))
print(filtered_list)


def power(n):
    return lambda a: a**n


power1 = power(1)
power2 = power(2)
power3 = power(3)
k=10
print(power1(k))
print(power2(k))
print(power3(k))