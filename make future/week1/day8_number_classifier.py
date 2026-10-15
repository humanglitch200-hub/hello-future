number = int(input("Print a number: "))

if number == 0: print("number is zero.")

elif number >= 1: 
    print("It's positive!")
    if number % 2 == 0: 
        print("Also Even")
    else: 
        print("Also odd")

else: print('number is negative')

