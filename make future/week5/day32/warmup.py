fruits = ["apple", "banana", "cherry", "date"]
del fruits[1]
del fruits[0]
del fruits[-1]
print(fruits)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
big =[n for n in numbers if n >= 4]
print(big)
big2 = big
print(big2 == big)

multiply = [n *2 for n in numbers]
print(multiply)
