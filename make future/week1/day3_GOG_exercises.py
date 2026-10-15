colors = ['red', 'blue', 'green']
colors[0]
colors[2]

b = colors  #Does not copy the list

squares = [1, 4, 7, 12]
sum = 0
for num in squares:
    sum += num
# print(sum)

#Value in collection

list = ['larry', 'curly', 'moe']
# if 'curly' in list:
    # print('cool')

#print the numbers from 0 to 99
# for i in range (100):
#     print(i)

#Access evry 3rd element in a list
# i = 0
# while i < len(a):
#     print(a[i])
#     i = i + 3

list = ['T', 'y']
list.append('g')
list.append('B')
# list[0:2] = 1
sorted(list)
print(sorted(list))
print(sorted(list, reverse = True))

strs =['c', 'BB', 'mmm', 'AAAA']
print(sorted(strs, key=len))
print(sorted(strs, key=str.lower))
sorted(strs, key=str.lower)

def MyFn(s):
    return s[-1]

print(sorted(strs, key=MyFn))        

from operator import itemgetter
grade = [('Freddy', 'Frank', 3), ('hari', 'lal', 4), ('future', 'trillionar', 10)]
sorted(grade, key=itemgetter(1,0))
sorted(grade, key=itemgetter(0, -1))

list.sort()

(x, y, z) = (42, 13, "hike")
print(z)
# (err_string, err_code) = foo()   #foo() is giving error!

nums = [1,2,3,4]
squares = [n * n for n in nums]

#Example with strings of ...
strs = ['Hello', 'and', 'goodbye']
shouting = [s.upper() + '!!!' for s in strs]


##Select values <= 2
nums = [2, 5, 7, 9, 1]
small = [ n for n in nums if n <= 2]

#Select fruits containing 'a', change to upper case
fruits = ['apple', 'cherry', 'banana', 'lemon']
afruits = [ s.upper() for s in fruits if 'a' in s]

dict ={}
dict['a'] = 'alpha'
dict['g'] = 'gamma'
dict['o'] = 'omega'
# print(dict)

if 'z' in dict: print(dict['z'])  #loop usig it avoides error
# print(dict.get('z'))

#Key are in a random order
for key in dict:
    print(key)

##Exactly the same as above 
for key in dict.keys():
    print(key)

##Get the .keys() list.
print(dict.keys())

##.values
print(dict.values())

##accesssing each key value
for key in sorted(dict.keys()):
    print(key, dict[key])

##Items
print(dict.items())

##Pair on eac h iteration
for k, v in dict.items(): print(k, '>', v)

##Dict Formatting
h = {}
h['word'] = 'garfied'
h['count']= 42
s = 'I want %(count)d copies of %(word)s' % h 

#Can also use str.format()
s =' I want {count:d} copies of {word}'. format(h)

var = 6
del var       #var no more (droped)

list = ['a', 'b', 'c', 'd']
del list[0] ##Delete first element
del list[-2:]   ##Delete last two elements
print(list)  ##['b]

dict = {'a': 1, 'b':2, 'c':3}
del dict['b']


##Files
#Echo the contents of a text file
f = open('foo.txt', 'rt', encoding='utf-8')
for line in f:   ##iterates over the lines of the file.
    print(line, end='')

f.close()


with open ('foo.txt', 'rt', encoding='utf-8') as f:
  for line in f:
      #Here line is a *unicode* string (Not geting it!!, but will certainly)
    break

with open ('write_test', encoding ='utf-8', mode='wt') as f:
    f.write('\u20ACunicode\u20AC\n')  
