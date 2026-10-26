#excercise 1:
def gen_power(exponent = 2 ):
    def power(base):
        print(base ** exponent)
    return power

square = gen_power(2)
square(3)


#Mutable default bug:
def add_item(item, basket=None):
    if basket is None:
       basket = []
    basket.append(item)
    return basket

add_item('hi')


#*args average:
def average(*nums):
    if not nums:
        return None
    avg = sum(nums)/ len(nums)
    print("Average:",avg)

average(0)


#**kwargs printer:
def describe(**info):
    for k, v in info.items():
        print(f"{k} : {v}")

infomration =({'name':'prem', 'age':28})
describe(**infomration)


#Order matters:
def mixed(a, b = 10, *rest, **kwargs):
    print(a, b, rest, kwargs)

mixed(2, 3, "mew", "hi", age=16, call="mew")

nums = [5, 10, 15]
#Unpacking on call:
def total(a, b, c):
    print(a, b, c)

#total(*nums) --it works
#total(nums)
   #--TypeError: total() missing 2 required positional arguments: 'b' and 'c'
