# new_file = open("Nandha's Corrrection_ Copy.txt", "r")
#
# for line in new_file:
#     print(line, end="")
#
# new_file.close()

# with open("Compre.txt", "r") as new_file:
# # with open("C:\Users\Jeyabalaganesh\Desktop\Compre.txt", "r") as new_file:
#
#     for line in new_file:
#         print(line, end="")


# with open("Compre.txt", "r") as new_file:
#     for line in new_file:
#         if "done" in line:
#             print(line)

# with open("Compre.txt", "r") as new_file:
#     line = new_file.readline()
#     """ Reads only one line"""
#     while line:
#         """For loop for the same printing"""
#         print(line, end="")
#         line = new_file.readline()


with open("Compre.txt", "r") as new_file:
    lines = new_file.readlines()

    print(lines)
    for line in lines:
        print(line, end="")
