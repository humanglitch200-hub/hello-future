#Finding min max:

# min(arg_1, arg_2, [, ..., arg_n], *[, key])
# max(arg_1, arg_2, [, ..., arg_n], *[, key])

#Accepts str, int, floart anything to compare , but least two have to there!


#It is a way to find mini or max from str:
min("abcdefghijklmnopqrstuvwxyz")
max("abcdWXYZ")
#output:  d
min('abcdWQJG')
#output: G
#this is happening becuase uppercase letters come before lowercase letters.


min("abc123ñ")
#output: 1
max("abc123ñ")
#output: ñ
#the uppercase A has a smaller numeric value than the lowercase a:

min("aA")
#output: A
max("aA")
#output: a

#Let's find min/max on word:
min(["Hello", "Python", "and", "welcome", "world"])
#output: 'Hello
max(["Hello", "Python", "and", "welcome", "world"])
#output: world

