basket = {'apple', 'orange', 'apple', 'pear', 'orange'}
print(basket)

a = set('abracadabraa')
b = set('alacazam')

print(a-b)  #letters in a but not in b
print(b | a) #lettters in a but not in b
print(a & b) #letters in a or b or both
print(a ^ b) #letters in a or b but nor both

a = {x for x in 'abracadabra' if x not in 'abc'}

fruits = [{'apple', 'avocado', 'apricot'}, {'banana', 'blueberry'}]
#print({*fruit for fruit in fruits}) it doesn't work on my python version but works!

#multielement set:
hex_hi= {
    "hi",
    "hi",
    "hi",
    "hi"
}

rgb_colors = {
    (51, 255, 87), #Green
    (51, 87, 255),#Blue
    (241, 196, 15),  
    (231, 76, 60),
}


# student = {
#     ("jane", 18, ["Math", "Physics", "History"]),
#     ("John", 19, ["English", "History", "philosophy"]),
# }    GIVES ERROR

#making set:
mew = set([1,23,234])

meww = set("Hello!")
print({"Hello!"})


#Comprehension:
#{expression for member in iterable [if confition]}

username = {
    "alice",
    "bob", 
    "charlie",
    "Charlie",
    "JOHN"
}

name = {name.lower().strip for name in username}
print(name)
#without this: {expression for member in iterable [if confition]} the output loks like:
#{<built-in method strip of str object at 0x70ce38631500>, <built-in method strip of str object at 0x70ce386314a0>,
# <built-in method strip of str object at 0x70ce386314d0>, <built-in method strip of str object at 0x70ce38631410>,
# <built-in method strip of str object at 0x70ce38631440>}
