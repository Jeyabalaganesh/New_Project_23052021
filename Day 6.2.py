
letters = "9a,45gj?@8u()!&7vf"
not_number = ""
alphabet = ""
number = ""

i = 0

for char in letters:
    if char.isalpha():
        alphabet = alphabet + char
        print("the index postion of char {0} in the string is {1}".format(char,i))


    elif char.isnumeric():
        number = number + char
    else:
        not_number = not_number + char
        
    i = i + 1

print("The alphabets in the given strings are {}".format(alphabet))
print("The numbers in the given strings are {}".format(number))
print("The not numbers in the given strings are {}".format(not_number))