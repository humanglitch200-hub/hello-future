# #printing from 1 to 10 by using while:
# i = 0
# while i <= 10:
#     print(i)
#     i += 1


# #counting from 5 to 1:
# n = 5

# while n >= 1:
#     print(n)
#     n -= 1
#     continue
# print("Blastoff!")

# #Asking for password and checking with while True:
# while True:
#     password = input("Enter password: ").lower()
#     if password =="python123":
#         print("Access granted")
#         break
#     else:
#         print("Try again!")
    

#asking user for positive number and ending after negative or 0:
# while True:
#       number = int(input("Enter a positive number: "))
#       if number <= 0:
#         break



#printing numbers 1 to 20:
n = 1
while n <= 20:
    if n % 3 == 0:
        n += 1         #if  I want to remove have to use % 3 != 0:   instead
        continue
    print(n)
    n += 1

   