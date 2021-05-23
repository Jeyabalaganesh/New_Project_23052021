# # name = "divakar"
# #
# # new_name = name
# #
# # print("{0} - {1}".format( name, id(name)))
# # print("{0} - {1}".format( name, id(new_name)))
# #
# # name = name + " Senthilvel"
# #
# # print()
# #
# # print("{0} - {1}".format( name, id(name)))
# # print("{0} - {1}".format( name, id(new_name)))
# #
# #
# # name = name + " M.E "
# #
# #
# #
# # print()
# #
# # print("{0} - {1}".format( name, id(name)))
# # print("{0} - {1}".format( name, id(new_name)))
# #
# #
# # name = name + " (Ph.D) "
# #
# #
# #
# # print()
# #
# # print("{0} - {1}".format( name, id(name)))
# # print("{0} - {1}".format( name, id(new_name)))
# #
# #
# #
# # ***********************************************************
#
# number  = 3.14
# new_number = number
#
# print(id(number))
# print(id(new_number))
#
# number += 1
#
#
# print(id(number))
# print(id(new_number))
#
#
# ****************************************************************

list = ["puffs", "tea", "coffee", "juice"]
new_list = list


print(id(list))
print(id(new_list))


list.append("bun")

print ()
print(id(list))
print(id(new_list))

print(list)
print (new_list)