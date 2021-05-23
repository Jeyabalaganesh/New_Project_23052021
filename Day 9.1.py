# name = 'Jeyabalaganesh G M.E'
# print(name.split(' '))
#
# numbers = '1,2,3,4,5,6,7'
# print(numbers.split(','))

number_string = input("enter any three numbers seo\parated by comma ")
list_name = number_string.split(",")
number =[]

for item in list_name:
    number.append(int(item))
print("Sum is {0}".format(number[0] + number[1] +  number[2]))

print(list_name)
print(number)


