set1 = {1,2,3,4,5}

print(set1)

new_list = list(set1)

print(new_list)

list1 = [2,4,6,8,10]
list2 = [4,16,36,64,100]

even = set(list1)
squares = set(list2)

print(even)
print(squares)

print(even.union(squares), len(even.union(squares)))
print(even.union(set1))

print(even.intersection(squares))

print(even.__sub__(squares))
print(squares.__sub__(even))


even.add(0)
print(even)
