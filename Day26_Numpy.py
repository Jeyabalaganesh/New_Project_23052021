import numpy as np

# data = np.array([[1, 2, 3], [4, 5, 6]])
# print(data)
# print(data.shape)
# print(data.size)
# print(data.ndim)
# print(data.dtype)
# print(data.nbytes)


# data1 = np.array([1, 2, 3, 4, 5, 6])
# print(data1)
# print(data1.shape)
# data2 = np.array([[1, 2, 3, 4], [1, 2, 3, 5], [8, 7, 1, 0]])
# print(data2)
# print(data2.shape)
# print(data2.size)

# data3 = np.array((1, 2, 3))
# print(data3)
#
# data4 = np.array(range(0, 10, 4))
# print(data4)
#
# data5 = 5 + np.zeros((2, 3), dtype=int)
# print(data5)
#
# one_array = np.ones((2, 3), dtype=int)
# print(one_array)
#
# empty = np.empty((2,3))
# print(empty)
# empty.fill(7)
# print(empty)
#
# single_step = np.full((10, 5), 3)
# print(single_step)

# xaxis = np.array(range(0, 11, 2))
# xaxis = np.arange(0, 11, 2)
# print(xaxis)
# yaxis = np.linspace(0, 10, 6)
# print(yaxis)
# logx= np.logspace(0, 10, 6)
# print(logx)


# data_id = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(data_id[2])
# print(data_id[-3])
# print(data_id[2:5])
# print(data_id[:5])
# print(data_id[2:])
# print(data_id[-1::-2])
# print(data_id[::-1])


data_set2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [11, 12, 13]])
# print(data_set2)
# print(data_set2[2, 1])
# print(data_set2[2:, 1:])
# print(data_set2[1:4, 1:4])
# print(data_set2[:-1:3, 1:])
# print(data_set2[:, 2])
# print(data_set2[2, :])


# one_d = np.arange(12)
# print(one_d)
# rshape = np.reshape(one_d, (4,3),order="C")
# print(rshape)
#
# rshape = np.reshape(one_d, (4,3),order="F")
# print(rshape)
#
# rshape = np.reshape(one_d, (3,4), order = "F")
# print(rshape)
#
# print(rshape.flatten(order="C"))
# print(rshape.flatten(order="F"))

data_set2 = np.array([[1, 3, 2], [6, 8, 7], [0, -2, 9], [1, 14, 8]])
print(data_set2)

# sorted_array = np.sort(data_set2)
print(np.sort(data_set2))
print(np.sort((data_set2), axis=0))
print("*"*25)

print((np.sum(data_set2, axis=1)))
print((np.sum(data_set2, axis=0)))
