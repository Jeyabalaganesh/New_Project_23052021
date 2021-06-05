"""
There are 4 types of polymorphism
1. Duck type
2. Operator overloading (Same operator can perform different operations under diff conditions)
3. Method Over ridding (Method in a same the name can be called upon differently based on the conditions)
4. Method Overloading (Same method can perform different operations under diff conditions)
"""

#  Operator Overloading

print(1 + 2)
print("jb" + "Ganesh")


class CoOrdinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        X = self.x + other.x
        Y = self.y + other.y
        s3 = CoOrdinate(X,Y)
        return s3


c1 = CoOrdinate(0, 4)
c2 = CoOrdinate(5, 6)
sum = c1.__add__(c2)
# sum = c1 + c2
print(sum.x, sum.y)


# Method Overloading

class Addition:
    def sum(self, a=0, b=0, c=0, d=0, e=0):
        s = 0
        s = a + b + c + d + e
        return s


s = Addition()
print()
print()
print(s.sum())
print(s.sum(1))
print(s.sum(1,3))
print(s.sum(1,5,7,6,2))

# Method Over ridding


class Parent:
    def print(self):
        print("This is parent")

    def print2(self):
        print("This is another part in the parent")


class Child(Parent):
    def print2(self):
        print("This is the over ridden method in the child")


obj1 = Parent()
obj2 = Child()

obj1.print()
obj2.print()

obj1.print2()
obj2.print2()

