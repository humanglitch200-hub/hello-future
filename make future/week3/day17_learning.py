cubes = [1, 2, 3, 4, 5]
cubes[3] = 64

#Adding
cubes.append(234)
cubes.append(4  ** 5)

#now cubes = [1, 2, 3, 4, 5, 234, 1024]

rgb = ["red", "greenn", "Yelo"]
rgba = rgb
id(rgb) = id(rgba)
#answer is True

correct_rgba = rgba[:]
correct_rgba[-1] = "Yello"

#Playing with letters:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E']

#calling all
letters[:] = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
len(letters)
 #answer is 7

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]

#printing x = [['a', 'b', 'c'][1, 2, 3]]


#while loop :
a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b

#OUTPUT IS: 0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,