class BankAccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"new balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return False
        self.balance - amount
        return True

    def show(self):
        print(f"{self.owner}: {self.balance}")


acc = BankAccount("prem", 100)
acc.deposit(200)
acc.withdraw(400)
