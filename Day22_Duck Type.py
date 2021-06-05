"""
Inheritance - The sub class is accessing the super class (all the variables)
Duck Type - The duck class has access to super class (Can be called only throught a particular variable
"""


class Flight:

    def __init__(self, l_w_r):
        self.len_wid_ratio = l_w_r

    def fly(self):
        if self.len_wid_ratio > 1:
            print("It can fly higher")
        elif self.len_wid_ratio == 1:
            print('It ca barely fly')
        else:
            print('It cant fly')

class Duck:

    def __init__(self):
        self.l_w_r = Flight(1.9)

    def walk(self):
        print("the duck walks gracefully")

    def swim(self):
        print("The duck swim very gently")

    def quack(self):
        print("The duck quack quack quack")

    def fly(self):
        self.l_w_r.fly()


class Pelicans:
    def walk(self):
        print("pelican walks like a duck")

    def swim(self):
        print("Pelican swim like a duck")

    def quack(self):
        print('pelican quack quack quack')


# def Duck_test(Duck):
#     Duck.walk()
#     Duck.swim()
#     Duck.quack()


Dinesh = Duck()
# Duck_test(Dinesh)
# print()
# Saravananan = Pelicans()
# Duck_test(Saravananan)
Dinesh.fly()
