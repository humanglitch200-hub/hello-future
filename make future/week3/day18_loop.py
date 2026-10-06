#both doing same thing: 
thislist = ["apple", "banana", "cherry"]

#Looping using for loop:
for i in range(len(thislist)):
    print(thislist[i])

#looping using while:
i = 0
while i< len(thislist):
    print(thislist[i])
    i += 1

#looping using list comprehension:
[print(x) for x in thislist]


#from ecxercise:
fruits = ['apple', 'banana', 'cherry']
newlist= ['apple' for x in fruits] 
#output: ['apple', 'apple', 'apple']



