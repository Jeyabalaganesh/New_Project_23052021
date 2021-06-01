import datetime

import pytz


class Account:
    """This is the simple class for showing the account of an user"""

    @staticmethod
    def _current_time():
        utctime = datetime.datetime.utcnow()
        return pytz.utc.localize(utctime)

    def __init__(self, name, amount):
        """ This function is meant for initialising the parameters"""
        self.account_holder = name
        self.__balance = amount
        self.transaction_list = [(Account._current_time(), amount, self.__balance)]
        print("The account has been started with \nName: {} \nInitial Deposit :{}".format(self.account_holder, self.__balance))

    def deposit(self, amount):
        """This function in the class account meant for deposit"""
        if amount > 0:
            self.__balance += amount
            self.show_balance("After the deposit the available balance is ")
            self.transaction_list.append((Account._current_time(), amount, self.__balance))

    def withdraw(self, amount):
        """This function in the class account meant for withdrawal"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.show_balance("After the withdrawal the available balance is ")
            self.transaction_list.append((Account._current_time(), -amount, self.__balance))

        else:
            print("Sorry you don't have the sufficient amount in the account ")
            self.show_balance("You only have the balance amount ")

    def show_balance(self, message):
        """This function in the class account meant for showing the balance """
        print(message + str(self.__balance))

    def transaction_history(self):
        for date, amount, balance in self.transaction_list:
            if amount > 0:
                trans_type = "Deposited"
            else:
                trans_type = "Withdrawn"
                amount = -amount

            print("{}, {}, {} and you have {}".format(date.astimezone(), trans_type, amount, balance))


if __name__ == "__main__":

    jb = Account("JB", 100)
    jb.deposit(1000)
    jb.withdraw(600)
    # jb.deposit(500)
    # jb.withdraw(500)
    # print(jb.balance)
    # print(jb.account_holder)
    # div = Account("Divakar", 2500)
    # div.show_balance("My balance is ")
    # jb.show_balance("My balance is ")
    # jb.withdraw(5000)

    jb.transaction_history()
    jb.show_balance("My balance is ")
    print(jb.transaction_list)
    print(jb.__dict__)
    print(jb.deposit.__doc__)
    print(jb._current_time())
    help(Account)

