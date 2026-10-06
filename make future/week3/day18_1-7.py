#printing biggest using for loop:
nums = [45, 12, 78, 33, 91, 12, 45]
biggest = nums[0]
for i in nums:
    if biggest < i:
        biggest = i       
print(biggest)

#printing lowest :
smallest = nums[0]
for i in nums:
    if smallest > i:
        smallest = i
print(smallest)

#couting things, what time they appear:
print(nums.count(12))
print(nums.count(45))


#Asking the user for 5 numbers and printing: sum, max, min, average and storing the list.
# nums =[]
# for i in range(5):
#     nums.append(float(input(f"Enter a number {i+1}: ")))

# if nums:
#     sum = sum(nums)
#     print(sum)
#     print(max(nums))
#     print(min(nums))
#     print(  sum/ len(nums)) 
# else:
#     print("No number entered.")

#printing where cat appears 'index'
words = ["cat", "dog", "elephant", "cat", "bird", "cat"]
for p, c in enumerate(words, start = 1):
    if 'cat' in c:
        print(p) 

#building new list for scores > 70:
scores = [55, 90, 72, 88, 100, 67, 45]
new_list = []
for score in scores:
    if score >= 70:
        new_list.append(score)

print(new_list)
print(scores)

#asking user for 6 numbers. Then asking for target and indexing it:
numbers = []
for n in range(6):
    numbers.append(format(input(f"Enter {n +1} number: ")))

target = input("Enter Target number.")
if target in numbers:
   print(numbers.index(target))

else:
        print('Not found!')
