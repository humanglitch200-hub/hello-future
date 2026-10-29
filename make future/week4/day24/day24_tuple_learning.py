#Tuples can be created without the parentheses:
fruits = "apple", "banana", "berry", "cherry"   #they can be with our parentheses
#(green, yelo) = fruits
#print(green) it prints [0]
#print(yelo) it prints [1]

#we also can use `*` for rest of the
(green, *yello, ch) = fruits   #'*' prints rest of the\
#after that one will be of last
print(ch)

print(fruits[0])
animals = fruits, ("cow", "buffalo", "mew")

#Tuple are immutable, BUT they countains multiple objects:
v = ([1,2,3],[3,2,1])

#also they support unpacking like lists:
x = [1,2,3]

print(0, *x, 4)   #'*x' == rest of the x


