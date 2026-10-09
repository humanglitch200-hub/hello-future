basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

'orange' in basket          #True
'crabgrass' in basket       #False

# Denonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')

print(a)
#{'a', 'r', 'b', 'c', 'd'}

print(a -b)                #letters in a but not in b
#{'r', 'd', 'b'}

print(a | b)               #letters of a & b both
#{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}

print( a & b)               #letters in both a and b 
#{'a', 'c'}

print(a ^ b)              #letters in a or b but not both 
#{'r', 'd', 'b', 'm', 'z', 'l'}


#LIST COMPRESSION:

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
#{'r', 'd'}          #same as a & b , but short and easy!



# USING POP():
books = ["Dragonsbane", "The Hobbit", "Wonder", "Jaws"]
read_books = []

read = books.pop(-1)
read_books.append(read)



#Using DEL:
books = [
     "Dragonsbane",
     "The Hobbit",
     "Wonder",       #Del deletes it.
     "Wonder",
     "Jaws",
     "Jaws",
]

del books[2]
#del books[-1]
#del books["Jaws"]
#del books[-3:-1]



