# number = [1, 2, 5, 100, 120, 150, 180, 235, 360]
# print(number)
# min_value = 99
# max_value = 200
#
#
# for index, num in enumerate(number):
#     if num > min_value:
#         stop = index
#         break
#
# del number[:stop]
#
# print(number)
#
#
# for index, num in enumerate(number):
#     if num > max_value:
#         stop = index
#         break
#
# del number[stop:]
#
# print(number)
#
#
# ****************************************
#
# number = [1, 2, 5, 100, 120, 150, 180, 235, 360]
# print(number)
# min_value = 99
# max_value = 200
#
# stop = 0
#
# for index in range(len(number)):
#     if number[index] >= min_value:
#         stop = index
#         break
#
# del number[:stop]
#
# start = 0
# for index in range(len(number)-1,-1,-1):
#     if number[index] <= max_value:
#         start = index + 1
#         break
#
#
# del number[start:]
# print(number)
# ************************************************************************


number = [1, 2, 5, 100, 120, 150, 180, 235, 360]
print(number)
min_value = 99
max_value = 200

for index in range(len(number)-1,-1,-1):
    if number[index] >= max_value or number[index] <= min_value:
        del number[index]

print(number)