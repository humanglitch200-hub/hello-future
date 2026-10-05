fruits = ['orange', 'apple', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.index('orange'))

print(fruits.pop())
print(fruits)

from collections import deque
queue = deque(["prem", "is", "Becoming", "More", "wise", "and", "intiligent"])
queue.popleft()   #The first to arrive now leaves

#putting what we get in code:
squares = []
for x in range(10):
    squares.append(x ** 2)

             #OR
squares = list(map(lambda x: x**2, range(10)))

             #OR
squares = [x**2 for x in range(10)]

[(x, y) for x in [1, 2, 3] for y in [3,1,4] if x != y]
#it makes new list by combining them like:
#[(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]


#and this is equivalent to:
combs = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            combs.append((x, y))
#same result

