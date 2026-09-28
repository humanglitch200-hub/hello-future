#ASKING THE  USER
username = input('Enter your name: ')
password = input('Enter password: ')
if username == 'admin' and password =='admin123':
    ask = input("Are you admin? (yes/no) ")
    if ask =='yes':
        print("Welcome, super admin")

    else:
        print("Welcome, admin")

elif username == 'user' and password =='user123':
    print("welcome, user")

else:
    print("Invalid credentials")


    

#asking for inforamtion
age = int(input("Enter your age: "))
day = input("It's a weekend (yes/no): ")

#storing ticet price:
ticket =[]

#looping
if age <= 5:
    ticket = '$0'

elif age > 5 < 17:
    if day == 'yes':
        ticket = '$12'

    else:
        ticket = '$8'


elif age > 18 < 64:
    if day == 'yes':
        ticket = '$15'

    else:
        ticket = '$12'

else:
    ticket = '$8'

#printing them
print(f"Your age is {age}")
print(f"Total bill is {ticket}")