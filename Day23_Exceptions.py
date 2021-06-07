# print "hai bro"
# x = 5/0
# lis = [10,20,30,5]
# lis[10]
# lis + 35
# d = {"a":1, "b":2, "c":3}
# print(d["e"])
# print(x)

# class EvenList(list):
#     def append(self, value):
#         if not isinstance(value, int):
#             raise TypeError("only integer values can be appended")
#         if value % 2 != 0:
#             raise ValueError("Only even numbers can appended")
#         super().append(value)
#
#
# e1 =EvenList()
# e1.append(4)

# def chkexcpetion():
#     print("This is the first line")
#     print("This is the second line")
#     raise Exception("This is an exception")
#     print("Line after exception1")
#     print("Line after exception2")
#
#
# def outerfunc():
#     print("This is the first line in outer fun")
#     chkexcpetion()
#     print("Line after the exception")
#     print("*********************")
#
# outerfunc()


# try:
#     x =5/0
# except ZeroDivisionError:
#     print("Denominator can not be a zero")
# except TypeError:
#     print("Check the denominator type")

# def getvalue(d, e):
#     try:
#         return d[e]
#     except KeyError:
#         return 0
#
#
# d = {"a": 20, "b": 15, "c": 32}
# print(getvalue(d, "b"))

def chk_exception():

    print("This is the first line")
    print("This is the second line")
    try:
        raise Exception("This is an exception")

    except Exception:
        print("Line after exception1")
        print("Line after exception2")


def outerfunc():
    print("This is the first line in outer fun")
    chk_exception()
    print("Line after the exception")
    print("*********************")


outerfunc()
