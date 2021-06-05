class BaseClass:
    no_of_base_class = 0

    def __init__(self):
        print("Executed the Base class")
        BaseClass.no_of_base_class += 1


class LeftClass(BaseClass):
    no_of_Left_class = 0

    def __init__(self):
        super().__init__()
        print("Executed the Left class")
        LeftClass.no_of_Left_class += 1


class RightClass(BaseClass):
    no_of_Right_class = 0

    def __init__(self):
        super().__init__()
        print("Executed the Right class")
        RightClass.no_of_Right_class += 1


class Subclass(RightClass, LeftClass):
    no_of_sub_class = 0

    def __init__(self):
        super().__init__()
        print("Executed the Sub class")
        Subclass.no_of_sub_class += 1


trial = Subclass()
print(trial.no_of_sub_class, trial.no_of_Left_class, trial.no_of_Right_class, trial.no_of_base_class)
trial.__init__()
print(trial.no_of_sub_class, trial.no_of_Left_class, trial.no_of_Right_class, trial.no_of_base_class)