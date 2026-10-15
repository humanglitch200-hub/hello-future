#make str input - folat.
# raw_input = input("Enter your score: ")
# score = float(raw_input)

#Another style with both combined (EASY WAY):
# scoree = float(input("Enter your score: "))

#The modulo operatoer:
name = "prem"
age = "18"
print("Hello, %s! You're %s years old" % (name, age))

#same but short method:
"Hello, %(name)s! You're %(age)s years old." % {"name": "Jane", "age": 25}

#Balancing:
"Balance: $%.2f" % 5425.2345231

print("Name: %s\nAge: %5s" % ("prem", 18))
#you use %5s to align the age value five positions to the right.

#avoid common probelm:
"The personal info is: %s " % (("prem", 18),)

#use of FORMAT {}
name = "prem"
age = 18
"HEllo {} you're {}. You'll surely be trellionar.".format(name, age)

#FOR better control over .format()
"HEllo {1} future {0}.".format(age, name)

#More styles:
"Hello, {name} You're {age}.".format(name='ram', age=12)

person = {"name": "Prremm", "age": 118}
"Hello, {name}! You're {age}. ".format(**person)


print("{:=^30}".format("MeW!"))

name = "prem lal"
age = " 18.1"
f"HELLO, It's me {name} at {age}. "

f"Hello, {name.upper()} You're of {age}. "
f"{[2**n for n in range(7, 11)]}"

#Datee coversion :
date = (9, 6, 2023)
f"Date: {date[0]:02}-{date[1]:02}-{date[2]}"

from datetime import datetime
date = datetime(2023, 9, 26)
print(f"Date: {date: %m/%d/%Y}")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"I'm {self.name}, and I'm {self.age} years old. "

    def __repr__(self):
        return f"{type(self).__name__}(name='{self.name}', age = {self.age} )"

prem = Person ("prem BHandari", 18)

print(f"{prem!s}") ## I'm prem BHandari, and I'm 18 years old.
print(f"{prem!r}")## Person(name='prem BHandari', age = 18 )


#ALL IN one let's see who won:

import timeit

name = 'Prem lal Bhandari'
age = 17
strings = {
    "Modulo operator": "'Name: %s Age: %s' % (name, age)",
    ".format() method": "'Name: {} Age: {}'.format(name, age)",
     "f_string": "f'Name: {name} Age: {age}'", 
}

def run_performance_test(strings):
    max_length = len(max(strings, key=len))
    for tool, string in strings.items():
        time = timeit.timeit(
            string,
            number=1000000,
            globals=globals()
        ) * 1000
        print(f"{tool}: {time:>{max_length - len(tool) + 6}.2f} ms")

run_performance_test(strings)

words = ['hi', 'bye', 'morning']
f"{'\n'.join(words)}"


# import psycopog2

# connection = psycopg2.connect(
#     database='bd',
#     user='user',
#     password='password'
# )
# cursor = connection.cursor()

# role = 'admin'

# query_modulo = "SELECT * FROM user WHERE role = '%s'" %role
# query_format = "SLECT * FROM users WHERE role = '{role}'".format(role=role)
# query_f_string = f"SELECT * FROM user WHERE role = '{role}'"

# cursor.execute(query_modulo)
# cursor.execute(query_format)
# cursor.execute(query_f_string)

# query_template = "SELECT * FROM user WHERE role = %s"
# cursor.execute(query_template, (role,))


greetinf_template = "{greeting} Pythonista!"

greeting_en = "Good Morning"
greeting_es = "cool"
greetng_fr = "night"

for greeting in (greeting_en, greeting_es, greetng_fr):
    print(greetinf_template.format(greeting=greeting))

#YOU CAN CHANGE  MODULE TO .FORMAT() WITH THE HELP OF FLYNT:
# $ flyth sample.py     - - on the shell(cmd)

name = input("Enter your name: ")
print(f"Hello, {name}!")
print(type(name))

