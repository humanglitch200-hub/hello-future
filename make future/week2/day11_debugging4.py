###WARNING  
# --THE CODE IS GIVEN BY DEEPSEEK 
# AND HAVE TO DEBUG 
# (SO, what you'll watch is debuged code!!)

#Debug.1:
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"

print(get_grade(85))

#Debug.2:
age = int(input("Enter your age: "))

if age >= 18:
    print("You can vote")
else:
    print("Too young")


#Debug.3:
def total_price(price, qty):
    result = price * qty
    return(f"Total: {result}")

final = total_price(50, 3)
print(f"Your final is: {final}")

