
item_no = 6
original = ["Idly", "Dosa", "Poori", "Pongal", "Vada"]
list = []


while item_no != 0:

    if item_no >= 1 and item_no <= 5:
        print("You have ordered {0}".format(original[item_no-1]))

        if item_no == 1:
            list.append("Idly")
        elif item_no == 2:
            list.append("Dosa")
        elif item_no == 3:
            list.append("Poori")
        elif item_no == 4:
            list.append("Pongal")
        elif item_no == 5:
            list.append("Vada")
    else:
        print("Enter the valid item no ")


    print (""" You can choose an item from the below menu 
           1. Idly
           2. Dosa
           3. Poori
           4. Pongal
           5. Vada
           0. if you are done """)

    item_no = int (input("Enter the item no "))


print("You have ordered {0}".format(list))
