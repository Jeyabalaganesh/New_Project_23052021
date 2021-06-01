import math


class Circle:
    def __init__(self, name, r, t=360):
        self.name = name
        self.radius = r
        self.theta = t
        self.print_data()

    def print_data(self):
        area = math.pi * math.pow(self.radius, 2) * (self.theta / 360)
        perimeter = 2 * math.pi * self.radius * (self.theta / 360)
        print("The area of the given {0} is {1:.2f}".format(self.name, area))
        print("The perimeter of the given {0} is {1:.2f}".format(self.name, perimeter))


cir1 = Circle("Full circle", 10)
cir2 = Circle("Half circle", 10, 180)
cir3 = Circle("Quarter circle", 10, 90)

