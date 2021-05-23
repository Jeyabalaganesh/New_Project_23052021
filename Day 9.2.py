# flower = [
#     "Jasmine",
#     "Rose",
#     "Lilly",
#     "Lotus",
# ]
#
# joined = ' *!% '.join(flower)
# print(joined)
#
# ********************************************


numbers = [1,2,3,4,5,75,86,96]

for index , num in enumerate(numbers):
    print(index,num)

for item in enumerate(numbers):
    # print(item)
    index , num = item
    print(index,num)
    