

menu = ["Idly", "Dosa", "Poori", "Pongal", "Vada"]
idmenu = []


idmenu = [ str (i) for i in range (1, len(menu)+1)]

# for i in range(1, len(menu)+1):
#     idmenu.append(str(i))

print (idmenu)

item_no = "~"

plate =[]

while item_no != "0":

    if item_no in idmenu:
        print("You have selected the item {0}".format(menu[int (item_no)-1 ]))
        plate.append(menu[int (item_no)-1 ])

    else:
        print("Enter the valid item no")

    print ("Choose any of the below items")

    for ind, item in enumerate(menu):
        print("{0}:{1}".format(ind+1, item))

    print(" Enter 0 if finished")



    item_no = str(input("Enter the id of the item "))




print ("The ordered items are {}".format(plate))