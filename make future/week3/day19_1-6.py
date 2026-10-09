#Rmoving duplicates with a loop:
nums = [1, 1, 2, 3, 3, 4, 5, 5, 5]
unique = []
for n in  nums:
    if n not in unique:
        unique.append(n)

print(unique)



#same list but remover duplicates with set() 
print(set(nums))



#Building new list with only numbers graater than 10:
nums = [12, 5, 8, 130, 44, 7, 99, 3]
grater_than_10 = []
for n in nums:
    if n > 10:
        grater_than_10.append(n)

print(grater_than_10)


#Building new list where each number is doubled:
nums = [1, 2, 3, 4, 5]
new_list = []
for n in nums:
    new_list.append(n + n)       #append + adding them.

print(new_list)        



#Making a list more than 3 letters and printing their length:
words = ['hi', 'hello', 'hey', 'world', 'yo']
n_list = []

for w in words:
    if len(w) > 3:
        n_list.append(w.upper())

#printing their lenght and The word:
for word in n_list:
    print(len(word), word)



#asking a user for a sentence, .split() it, count how many times each word appears:
sentence = str(input("Enter a sentence: "))
word = sentence.split()

counts = {}                          
for w in word:
    if w in counts:
        counts[w] += 1

    if w not in counts:
        counts[w] = 1
        
for w in counts:
    print(counts[w], w)

    

    
    


