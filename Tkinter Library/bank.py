class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, "r") as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, "w") as file:
            file.write(str(self.balance))

class Cheking(Account):
    type = "cheking"
     
    def __init__(self, filepath, fee):
        self.fee = fee
        Account.__init__(self, filepath)

    def trasfer(self, amount):
        self.balance = self.balance - amount - self.fee



cheking = Cheking("balance.txt", 1)
cheking.trasfer(10)
print(cheking.balance)
cheking.commit()






"""
account = Account("balance.txt")
print(account.balance)
account.withdraw(100)
print(account.balance)
account.commit()
"""
