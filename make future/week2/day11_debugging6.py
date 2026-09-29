###WARNING  
# --THE CODE IS GIVEN BY DEEPSEEK 
# AND HAVE TO DEBUG 
# (SO, what you'll watch is debuged code!!)
#also it is the part of day11_debugging4.py

#Debugging.5:
is_member = input("Are you a member? (yes/no): ").lower()

if is_member == "yes":
    print("Discount applied")
else:
    print("No discount")


#Debugging.6:
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

number = 7
if is_even(number) == True:
    print("Even")
else:
    print("Odd")
