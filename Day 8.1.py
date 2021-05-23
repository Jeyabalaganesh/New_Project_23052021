# even = [2,4,6,8,10]
# odd = [1,3,5,7,9]
#
#
# numbers = even.extend(odd)
#
# print(even)
# print(odd)
# print(numbers)
#
#
# *******************************************************

# even = [2,4,6,8,10]
# odd = [1,3,5,7,9]
#
#
# even.extend(odd)
#
# print(even)
# print(odd)
#
# even.sort()
#
# print(even)
#
# even.sort(reverse=True)
#
# print(even)
#
# ***********************************************************

#
#
# even = [2,4,6,8,10]
# odd = [1,3,5,7,9]
#
#
# even.extend(odd)
#
# print(even)
#
# # new_even = even.copy()
# new_even = even
#
# new_even.sort()
#
# print()
# print(even)
# print (new_even)
#
# new_even.sort(reverse=True)
#
# print()
# print(even)
# print (new_even)
#
# print(id(even))
# print(id(new_even))
#
#
# ************************************************************

    even = [2,4,6,8,10]
    odd = [1,3,5,7,9]


    even.extend(odd)

    new_list = sorted(even)

    print(new_list)

    print(sorted("aiqujfHKW92,;", key = str.casefold))



