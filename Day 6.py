print("Welcome to the class day 2")
letters = "9a,45gj?@8u()!&7vf"
not_number = ""
alphabet = ""
number = ""

for char in letters:
    if char.isalpha():
        alphabet = alphabet + char
    elif char.isnumeric():
        number = number + char
    else:
        not_number = not_number + char


print("The alphabets in the given strings are {}".format(alphabet))
print("The numbers in the given strings are {}".format(number))
print("The not numbers in the given strings are {}".format(not_number))