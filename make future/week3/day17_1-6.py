#Printing each color and their index:
colors = ['red', 'green', 'blue']
for c in colors:
    print(c)
    print(colors.index(c))

#Printing first, last, middle two and reversed copy:
nums = [4, 8,15, 16, 23, 42]
print(nums[0])
print(nums[-1])
print(nums[2:4])
print(nums[::-1])
print(nums[::2])


#Remove .append and do certain things:
task = []
task.append("code")
task.append("chill")
task.append("code")
task.remove("chill")
print(task)


#Printing , sorting, reverse, max and min:
scores = [55, 90, 71, 88, 100]
scores.sort()
print(scores)

scores.reverse()
print(scores)

print(max(scores))
print(min(scores))


#asking for a number for five times and priting it at lsat:
# my_list = []

# for _ in range(5):
#     num = int(input("Enter a number: "))  #Helped by AI!
#     my_list.append(num)

# print(my_list)
# print("Sum:", sum(my_list))   



asking = input("Enter a sentence: ")
word = asking.split()

print("Word count: ", word.count(word))
print(word[:0])
print(word[-1])
print(sorted(word))




