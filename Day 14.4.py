classic= { "puffs" : "Crunchy",
           "coffee" : "Tasty",
           "tea"    : "not good",
           "cake"   : "not bad"

}

while True:
    item = input("Enter the item you would like to order, quit for leave ")
    if item.casefold() == "quit" :
        break
    print("You have ordered {0} which is {1}".format(item, classic.get(item.casefold(), "sorry" + item + " is not available")))
    # if item in classic:
    #     print("You have ordered {0} which is {1}".format(item, classic[item.casefold()]))
    # else:
    #     print("You have entered item {} which is not available in classic".format(item))
