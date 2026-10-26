def my_function(*args):
    print("Type:", type(args))
    print("First argument:", args[0])
    print("Second argument:", args[1])
    print("All argument:", args)
    # print("Second argument:", args[4])  get error!

my_function("Emil", "Elone", "Jeff", "mew")

def my_function(greeting, *names):
    for name in names:
        print(greeting, name)

my_function("Hello", "prem", "elone")
print()

def my_function(**myvar):
    print("Type: ", type(myvar))
    print("Name: ", myvar["name"])
    print("Age: ", myvar["age"])
    print("All data: ", myvar)

my_function(name = "Tobais", age = 28, city = "Bergen")

def my_function(username, **details):
    print("Username: ", username)
    print("Additional details: ")
    for key, values in details.items():
        print(" ", key + ":", values)

my_function("email123", age= 25, city= "kathmandu", hobby = "coding")


#Unpacking a dictionary into keyword arguments:
def my_function(fname, lname):
    print("Hello", fname, lname)

person = {"fname":"Emili", "lname":"Refsnes"}
my_function(**person)

def fib(n):

    a, b = 0,1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

fib(2000)


def ask_ok(prompt, retries= 4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries -1
        if retries < 0:
            raise ValueError('Invalid user responce')
        print(reminder)



i = 5 
def f(arg=i):
    print(arg)
i = 6
f()

def f(a, L =None):
    if L is None:
        L = []
    L.append(a)
    return L
print(f(1))
print(f(8))
print(f(3))


