def Pressure():
    print("""
Data entering format:
Pressure value as a whole number and Unit as atm for atmospheric 
                                                Pa for Pascal
                                                Bar for Bar     
          """)

    a= str (input("Enter the pressure value (Space) unit in the above format "))
    temp = a.split()
    x , y = temp
    z = float (x)

    if y == "atm":
        at = z
        pa = z * 10135
        bar = z * 1.0135

    elif y == "Pa":
        at = z / 101325
        pa = z
        bar = z / 100000

    elif y == "Bar":
        at = z / 1.0135
        pa = z * 100000
        bar = z

    else:
        print("You are entering the pressure value in wrong format")
        return()

    print()
    print("Pressure in atm {:.2f}".format(at))
    print("Pressure in Pascal {:.2f}".format(pa))
    print("Pressure in Bar {:.3f}".format(bar))

    return()



Pressure()
