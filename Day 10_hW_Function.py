def factorial(n):
    value = 1
    for i in range (n):
        value  = value * (i+1)
    return value


print("Welcome to the prgrame to calculate factorial")

f = int ( input ("Enter any integer to calculate its factorial "))
value = factorial(f)

print("Factorial of {0} is {1}".format(f, value))
print()





