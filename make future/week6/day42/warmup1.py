class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(f"{self.name} woof")

d = Dog("Rex")
d.bark()

try:
    class Broken:
        def f():
            print("meww")
    hi = Broken("mew")
    hi.Broken()

except TypeError:
    print("Type Error occure")
    del Broken

class Counter:
    def __init__(self):
        self.count = 0
    def inc(self):
        self.count += 1
a = Counter()
b = Counter()
a.inc()
a.inc()

class bank:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        self.log("deposit")
    def log(self, action):
        print(f"{action} balance: {self.balance}")

b = bank(100)
b.deposit(50)

def add_name(names, name):
    names.append(name)

names = []
add_name(names, "Jeff"); print(names)

class Namelist:
    def __init__(self, names):
        self.names = []

    def add(self, name):
        self.names.append(name)

nl = Namelist(0); nl.add("Alice"); print(nl.names)



