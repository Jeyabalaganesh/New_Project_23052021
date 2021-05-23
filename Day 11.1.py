def palindrom(sen):
    name =""
    for char in sen:
        if char != " ":
            name += char
    rev_string =  name[::-1]
    print(name)
    print(rev_string)
    return name.casefold() == rev_string.casefold()


def sen_palindrom(sen):
    name =""
    for char in sen:
        if char != " ":
            name += char
    return palindrom(name)

line = str (input ("Enter any sentence to check for palindrome "))

if (palindrom(line)):
    print("The entered string \"{}\" is a palindrom ".format(line))
else:
    print("The entered string \"{}\" is not a palindrom ".format(line))