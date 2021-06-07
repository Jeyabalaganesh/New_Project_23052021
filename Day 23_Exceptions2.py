# def fun(a):
#     try:
#         return 10/a
#     except:
#         return 0
#
# print("It worked {}".format(fun(0)))


# import random
#
# exception_list=[TypeError, NameError, AttributeError, SyntaxError, None]
#
# try:
#     expt = random.choice(exception_list)
#     print("Selected the error as {}".format(expt))
#     if expt:
#         """if expt != None"""
#         raise expt("An error")
# except TypeError:
#     print("Type error")
# except NameError:
#     print("Name error")
# except AttributeError:
#     print("Attribute error")
# except SyntaxError:
#     print("syntax error")
# else:
#     print("There is no exception")
# finally:
#     print("This will always be executed")

#
# class InvalidWithdrowal(Exception):
#     pass
#
# raise InvalidWithdrowal("You have too much than you have")

a = int(input("Enter the value of a: "))

if a >= 2:
    print(a)
else:
    raise Exception("The vale is too small")
