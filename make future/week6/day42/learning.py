class Dog:
    def __init__(self, name):
        self.name=name
        self.toys = [] #each instance gets its own list.
    def add_toy(self, toy):
        self.toys.append(toy)

d1 = Dog("Rex")
d2 = Dog("Fido")
d1.add_toy("ball")
print(d1.toys)
print(d2.toys)

class Bank:
    def __init__(self, balance =0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        self.log("deposit")
    def log(self, action):
        print(f"{action}: balance={self.balance}")

b = Bank()
b.deposit(100)

class Phonebook:
    def __init__(self, filename):
        self.fielname = filename
        self.contacts = []
        self.load()
        
#Creating instances:
# p = Phonebook("data.json")
# print(isinstance(p, Phonebook))

