def find_sum(lst):
    a_sum = 0
    for element in lst:
        a_sum += float(element)
    return a_sum

def find_length(lst):
    length = 0
    for emement in lst:
        length += 1
    return length

def mean(lst):
    return find_sum(lst) / find_length(lst)

print(mean([1,2,3,6,2]))

def add_value(x, constant = 3.14):
    return x + constant

print(add_value(6))
print(add_value(6))

def sum_or_diffrence(a, b, return_sum=True):
    if return_sum:
        return a + b
    else:
        return a - b

print(sum_or_diffrence(10, 7))
print(sum_or_diffrence(10,4,False))

def sum_and_difference(a, b):
    a_sum = a 
    a_difference = a - b
    return a_sum, a_difference

sum_1, diff_1 = sum_and_difference(15, 23)
print(sum_1, diff_1)

squares = "{0} times {0} equals {1}".format(3,9)
print(squares)

population = "{name}'s population is {:,}% million".format(203454, name="Brazil")
print(population)

bad_chars = ["'", ",", ".", "!"]
string = "We'll remove apostrophes, commas, periods, and exclamation marks!"

for char in bad_chars:
    string = string.replace(char, "")

print(string.title())

split = "1980-12-08".split('-')
print(split)

first = "this is me."[:4]
print(first)

apps_names = []
for row in apps_names[1:]:
    name = row[1]
    apps_names.append(name)

print(apps_names)

class MyClass:
	def __init__(self, param_1):
		self.attribute = param_1
	def add_20(self):
		self.attribute += 20

mc_3 = MyClass(10) 
mc_3.add_20()

from datetime import datetime as dt


eg_2 = dt.strptime("15/08/1990 08:09:30", 
                   "%d/%m/%Y %H:%M:%S")

eg_2_str = eg_2.strftime("%B %d, %Y at %I:%M %p")
print(eg_2_str)

eg_2_time = eg_2.time()
print(eg_2_time)


name = "prem"
age = 21
print(name, type(name))

num_str = "50"
result = int(num_str) + 25

print(result)

float = float(num_str)
print(float)

first = "Python " * 3
second = "programming"

print(type())
