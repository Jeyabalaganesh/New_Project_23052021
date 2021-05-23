

menu = ["Idly", "Dosa", "Poori", "Pongal", "Vada"]
item_no = "~"
plate =[]

while item_no != 0:

    if item_no in range (1, len(menu)+1):
        plate.append(menu[item_no-1])

    elif item_no != "~":
        print("Enter the valid item no")

    print ("Choose any of the below items")

    i = 0
    for item in menu:
        i+=1
        print("{0}:{1}".format(i, item))
    print(" Enter 0 if finished")



    item_no = int(input("Enter the id of the item "))




print ("The ordered items are {}".format(plate))