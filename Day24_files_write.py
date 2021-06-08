scholars = ["jb", "Diva", "Arun", "Sarav", "Dinesh"]

# with open("scholars.txt", "w") as new_file:
#     for scholar in scholars:
#         print(scholar, file=new_file)


# with open("scholars1.txt", "w") as new_file:
#     for scholar in scholars:
#         # new_file.write(scholar)
#         print(scholar, file=new_file)
#
# mech_scholars = []
# with open("scholars.txt", "r") as new_file:
#     for name in new_file:
#         mech_scholars.append(name.strip("\n"))
#
# print(mech_scholars)

# muthalvan = ("ARR", 2000, ("song1", "song2", "song3"))

# with open("file.txt", "w") as new_file:
#     print(muthalvan, file=new_file)
#
# with open("file.txt", "r") as new_file2:
#     lines = new_file2.readlines()
#
# print(lines)
# file = eval(lines[0])
# print(file)
#
# composer, year , songs = file
# print(composer)
# print(year)
# print(songs)

# with open("scholars.txt", "w") as new_file:
#     for scholar in scholars:
#         # new_file.write(scholar)
#         print(scholar, file=new_file, flush =True)
#         print(scholar, file=new_file)


scholars2 = ["Jinshah", "Peter", "Ravi", "Michael"]
# with open("scholars1.txt", "x") as new_file:
#     """x keyword return an error if a file is already existed in the same name"""
#     for scholar in scholars2:
#         print(scholar, file=new_file)

with open("scholars.txt", "a") as new_file:
    for scholar in scholars2:
        print(scholar, file=new_file)
