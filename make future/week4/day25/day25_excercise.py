#trying duplicates:
fruits = {'apple', 'banana', 'mango', 'blue berry', 'pine apple'}

# fruits.append('water mellon')   --- AttributeError: 'set' object has no attribute 'append'
print(fruits)  
#print(fruits[0])                 --- TypeError: 'set' object is not subscriptable


#Dedupe:
l = [1, 2, 2, 3, 4, 4, 4, 5, 1]
print(l.count(1))
for n in l:
    if l.count(n) == 1:
        print(n, 'is unique')

lset = set(l)
print(lset)
print(len(lset))
s_lset = sorted(lset)
print(s_lset)

#union/ intersection/ diffrence:
m = {1, 2, 2, 3, 4, 4, 4, 5, 1}
n = {8,7,6,5,34,3,2,1}
print(m | n)
print(m & n)
print(m - n)
print(m ^ n, 'mew')

#Common friends:
elones_frnd = {'jeff', 'mac', 'mew'}
prems_frnd = {'gets', 'mark', 'mew'}
elones_frnd & prems_frnd   #friend of both
elones_frnd - prems_frnd #symmetric diff
elones_frnd | prems_frnd #friends of all

#empty set trap:  they are not diff, buit the process of making them is!
a ={'mew'}
b = set('mew')
print(type(a))
print(type(b))


#sorted unique:
sentence = ('my self future trellionare!')
print(sorted(set(sentence.split())))


prem = {'coding', 'marsh', 'tech', 'space', 'business', 'know', 'travelling', 'loving', 'walking'}
elone = {'coding', 'research', 'read', 'know', 'business', 'rocket science', 'tech', 'space', 'marsh'}

print(prem ^elone)