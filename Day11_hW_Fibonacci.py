def fibonacci(n):
    a=0
    b=1
    sum = 0
    print(a)
    print(b)

    for i in range (n-2):
        sum = a + b
        a = b
        b = sum
        # return(sum)
        print(sum)


f= int (input ("Enter the number of Fibonacci series to be gernerated on screen (atleast 2) "))


print("{}".format(fibonacci(f)))