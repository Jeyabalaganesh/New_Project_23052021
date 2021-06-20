import numpy as np

# print(np.indices((2,3)))
data_set2 = np.array([[6, 2, -3], [1, 5, 7], [5,8,9]])
print(data_set2)
print("*")
new = np.full((3,3), 1)


# print(np.diagonal(data_set2))
print(np.diag(data_set2))
# print(np.trace(data_set2))
print(np.triu(data_set2))
print(np.tril(data_set2))

print(np.diag(np.diag(new)))

