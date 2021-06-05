class CheckSelf:
    number = 10

    def increment_sum(self):
        CheckSelf.number += 1
        return CheckSelf.number

    def print_id(self):
        print("The if of {} is {}".format(self, id(self)))
        print("The incremented number is {}".format(self.increment_sum()))


obj1 = CheckSelf()
obj1.print_id()
print("The if of {} is {}".format(obj1, id(obj1)))
print()
obj2 = CheckSelf()
obj2.print_id()
print("The if of {} is {}".format(obj2, id(obj2)))


