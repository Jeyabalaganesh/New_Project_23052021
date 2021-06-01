class Box:
    def __init__(self, name, a, b=1.0):
        self.name = name
        self.length = a
        self.breath = b
        self.print_data()

    def print_data(self):

        if self.breath == 1.0:
            area = self.length * self.length
            perimeter = 2 * (self.length + self.length)
        else:
            area = self.length * self.breath
            perimeter = 2 * (self.length + self.breath)

        print("The area of the given {0} is {1:.2f}".format(self.name, area))
        print("The perimeter of the given {0} is {1:.2f}".format(self.name, perimeter))


square = Box("Square", 10.2)
rect = Box("Rectangle", 20.3, 10.0)

