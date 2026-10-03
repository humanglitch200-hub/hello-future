import time
for n in range(2, 10):
    for x in range(2, n):
        if n % n == 0:
            print(f"{n} equals {x} * {n//x}")
            break

number = 5
while number != 0:
    print(number)
    number -= 1

    #If you minus number by 2 you get an error.


time.sleep(3)    #Time breaking 'nice one!'

#Short script that demonstarates how the break satement works:
number = 6

while number > 0:
    number -= 1
    if number == 2:
        break        #here you can use 'continue'
    print(number)

print("Loop ended")

#incriment game to break in while:
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1


#Let's play with clors:
colors = ["red", "green", "blue", "white"]

while colors:
    color = colors.pop(-1)
    print(f"Processing color: {color}")


#Let's try looping:
line = input("Enter a word: ")

while line != "stop":
    print(line)
    line = input("Enter a word: ")

#same same but diffent.
while (line := input("Type some text: ")) != "stop":
   print(line)

# use of dots ...
condition_1 = 1
condition_2 = 1
while True:
    if condition_1:
        break
    ...
    if condition_2:
        break
    ...             #it is like break. It is Break!!

#I can use it like:
    if condition_1 == condition_2:
        print("They are same")
        break

    if condition_2 == 1:
        print(f"condition_2 is = {condition_2} ")
        break

    else:
        print(f"condition_2 is less than = 1 ")
        break


#BREAK:
while True:
    name = input("Enter name (or 'quit'): ").lower().split()
    if name == 'quit':
        break
    print(f"helo {name}")
print("Done.")

#continue:
for i in range(1, 11):
    if i % 2 == 0:
        continue   #skip even number
    print(i)       #only odd print

#while loop:
n = 5
total = 0
while n > 0:
    total += n
    n -= 1
print(total)





