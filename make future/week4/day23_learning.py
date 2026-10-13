thisdict = {'hi': 'hello'}
# print all key names in the dictionary, one by one:
for x in thisdict:
    print(x)

#print all values in the dictonary, one by one:
for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)

for x in thisdict.keys():
    print(x)

for x, y in thisdict.items():  #looping over keys, values by using items():
    print(x, y)

myfamily = {
    "child1" : {
        "name": ["Sushil", "Deepa", "something"],
         "age" : 26
    },

    "child2" : {
        "name" : "Bamdev",
        "age"  : 21
    }, 
    "child3" : {
        "name" : "Prem",
        "age"  : 18
    }
}
print(myfamily["child1"]["name"][0])
for x, obj in myfamily.items():
    # print(obj.values())

    for y in obj:
        print(y + ':', obj[y])


#LOOPING TECHNIQUES:
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v, k)
#It feels like using **k**v.

#print with index number
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

questions = ['name', 'quest', 'favourite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print(f'What is you {q}? It is {a}.')

for i in reversed(range(1, 10, 2)):
    print(i)

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(set(basket)):
    print(i)

import math
raw_dta = [56.3, float('Nan'), 10]
filtered_data = []
for value in raw_dta:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)


config = {
    "color": "green",
    "width": 42,
    "height": 100,
    "font": "courier",
}
config["font"] = "Helvetca"
config["height"] = "5.8f"
config["name"] = "Rice"
print(config)

class Number:
    def __init__(self, value):
        self.valu = value

print(Number(42).__dict__)

a_dict = {(1, 1): "a", (1,2): "b", (2, 1): "c", (2, 2): "d"}


#soting words key = len
words = ["banana", "pie", "washington", "book"]
sorted(words, key=len)

words = sorted(["banana", "pie", "washington", "book"], key=str.lower)

def add(x, y):
    return x + y

def reverse_word(word):
    return word[::-1]

word = ["cookie", "banana", "donut", "pizza"]
print(sorted(word, key=reverse_word))