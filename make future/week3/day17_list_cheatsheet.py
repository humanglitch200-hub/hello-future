'''
LIST CHEAT SHEET - WEEK 3 Day 17
Keep this file. Read it when you forget syntax.
'''

# ─── CREATE ───
empty = []                              #empty list
nums = [1, 2, 3, 4]                     #nums list
zero = [0]  * 4                         #list of zero
copy1 = nums.copy()                     #makes a shallow copy.
copy2 = nums[:]                         #copy the whole list.
print("CREATE: ", nums, zero, copy1, copy2)

# ─── READ / INDEX ───
print("nums[0]:  ", nums[0])            #prints first nuber of nums  
print("nums[-1]: ", nums[-1])           #index, print last one!
print("nums:     ", len(nums))          #find how many numbers are there.
print("nums:     ", nums.index(1))      #it index where is '1' in nums.
     
# ─── SLICE ───
nums[1:3]          #prints 2st number and 3th one!
nums[:2]           #print first two
nums[::2]          #prints 1st and 3rd, starting from Begging : [1, 3] 
nums[-1]           #prints last number
nums[-2:]          #print last and second last number

# ─── ADD ───
nums.insert(0, 2)            #insert 2 in 0th in nums
nums.append(3)               #add 3 at last of nums
nums.extend(zero)            #extend zero in nums

print ("ADD: ", nums)

# ─── REMOVE ───
last = nums.pop(-1)              #pop 6 at last of nums
first = nums.pop(0)              #Remove 1th number from ther list
nums.remove(3)                   #remove 3 from nums

# ─── SORT / REVERSE ───
nums.sort()                                   #sort changes the list   
new_nums = sorted(nums, reverse = True)       #sorted returns a new list
print("soretd():", new_nums, "| original:", nums)

nums.reverse()                #It reverse the nums 

# ─── SEARCH ───
min(nums)                      #Find min in nums
nums.count(1)                  #show how many times 1 appear in nums
max(nums)                      #Find max in nums
1 in nums                      #Find if there is any x in nums

# ─── LOOP ───
len(nums)                      #Tells how many numbers num has
for n in nums:                 # for 'n' in 'nums'
    break


for i in nums:                 #print i in nums number by number individually
    break

# ─── LOOP — index + value (the pattern you'll use most) ───
for i, item in enumerate(nums):
    print(f"index {i} - {item}")

# ─── LOOP — while with a REAL body ───

# temp = nums.copy()                     #Works on copy 
# while len(nums) > 0:
#     print("poping:", temp.pop())       #This line changes the condition
# print("temp empty: ", temp)

print(nums)
