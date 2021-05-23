def Length():
    print("""
Data entering format:
Length value as a whole number and Unit as  m for Meter 
                                            ft for feet
                                            cm for centimeter
                                            mm for millimeter    
          """)

    a= str (input("Enter the Length value (Space) unit in the above format "))
    temp = a.split()
    x , y = temp
    z = float (x)

    if y == "m":
        meter = z
        feet = z * 3.281
        centi = z * 100
        milli = z * 1000

    elif y == "ft":
        meter = z / 3.281
        feet = z
        centi = z / 3.281 * 100
        milli = z / 3.281 * 1000

    elif y == "cm":
        meter = z / 100
        feet = z / 100 * 3.281
        centi = z
        milli = z * 10

    elif y == "mm":
        meter = z / 1000
        feet = z / 1000 * 3.281
        centi = z / 10
        milli = z

    else:
        print("You are entering the length value in wrong format")
        return()

    print()
    print("Length in Meter {:.3f}".format(meter))
    print("Length in Feet {:.2f}".format(feet))
    print("Length in Centi Meter {:.1f}".format(centi))
    print("Length in Milli meter {:.0f}".format(milli))

    return()



Length()
