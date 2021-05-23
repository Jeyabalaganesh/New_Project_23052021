def temperature():
    print("""
Data entering format:
Temperature value as a whole number and Unit as K for Kelvin 
                                                C for Celcius
                                                F for Farenheit     
          """)

    a= str (input("Enter the temperature value (Space) unit in the above format "))
    temp = a.split()
    x , y = temp
    z = float (x)

    if y == "K":
        c = z - 273
        f = (z- 273) * (9/5) + 32
        k = z

    elif y == "C":
        c = z
        f = ( z * (9/5)) + 32
        k = z + 273

    elif y == "F":
        c = (z - 32) * ( 5/9 )
        f = z
        k = ((z - 32) * ( 5/9 )) + 273

    else:
        print("You are entering the temperature value in wrong format")
        return()

    print()
    print("Temperature in Celcius {:.2f}".format(c))
    print("Temperature in Farenheit {:.2f}".format(f))
    print("Temperature in Kelvin {:.2f}".format(k))

    return()



temperature()
