letters = "911111a,45gj?@8u()!&7vf"

for i in range(len(letters)):
    if not letters[i].isnumeric():
        print("The non numeric char {0} in position {1} ".format(letters[i],i))
