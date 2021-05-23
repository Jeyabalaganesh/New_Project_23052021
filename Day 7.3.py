

menu = ["Idly", "Dosa", "Poori", "Pongal", "Vada"]
item_no = "~"
plate =[]

while item_no != 0:

    if item_no in range (1, len(menu)+1):
        plate.append(menu[item_no-1])

    else:
        print("Enter the valid item no")

    print ("Choose any of the below items")


    for ind, item in enumerate(menu):
        print("{0}:{1}".format(ind+1, item))

    print(" Enter 0 if finished")



    item_no = int(input("Enter the id of the item "))




print ("The ordered items are {}".format(plate))