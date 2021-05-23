classic = ["puffs", "Tea", "milk", "Priya", "coffee" ]

for pos in range(len(classic)):
    if classic[pos].casefold()  == "priya" :
        break


print ("The position of {0} in classic is {1}".format(classic[pos], pos ))
