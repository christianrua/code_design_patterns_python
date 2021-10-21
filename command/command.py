
from abc import ABC
from enum import Enum

class BanKAccount:
    OVERDRAFT_LIMIT = -500

    def __init__(self, balance = 0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited {amount}, balance = {self.balance}') 

    def withdraw(self, amount):
        if self.balance - amount >= BanKAccount.OVERDRAFT_LIMIT:
            self.balance -= amount
            print(f'withdrew {amount}, balance = {self.balance}')
            return True
        return False       


    def __str__(self):
        return f'Balance = {self.balance}'


class Command(ABC):
    def invoke(self):
        pass

    def undo(self):
        pass


class BankAccountCommand(Command):
    class Action(Enum):
        DEPOSIT = 0
        WITDRAW = 1

    def __init__(self, account, action, amount):
        self.account = account
        self.action = action
        self.amount = amount
        self.success = None

    def invoke(self):
        if self.action == self.Action.DEPOSIT:
            self.account.deposit(self.amount)
            self.success = True

        elif self.action == self.Action.WITDRAW:
            self.success = self.account.withdraw(self.amount)

    def undo(self):
        if not self.success:
            return 

        if self.action == self.Action.DEPOSIT:
            self.account.withdraw(self.amount)
        elif self.action == self.Action.WITDRAW:
             self.account.deposit(self.amount)           

if __name__ == '__main__':
    ba = BanKAccount()  
    cmd = BankAccountCommand(
        ba, BankAccountCommand.Action.DEPOSIT, 100
    )                  
    cmd.invoke()
    print(f'After $100 deposit: {ba}')

    cmd.undo()
    print(f'$100 deposit undone: {ba}')

    illegal_cmd = BankAccountCommand(
        ba, BankAccountCommand.Action.WITDRAW, 1000
    )
    illegal_cmd.invoke()
    print(f'After impossible withdrawal: {ba}')
    illegal_cmd.undo()
    print(f'After undo: {ba}')