## The basic shape

def greet(name):
    return f"Hello, {name}!"

message = greet("prem")
print(message)


#With function cleaner, reusable code writing:

def evaluate_job(salary, remote, interest, training, distance):
    if salary < 15000:
        return "Too low"
    elif salary >= 15000 and (remote or distance <= 10) and interest and training:
        return "⭐ Strongly recommended"
    #.......
    return "X Not recommended"

result = evaluate_job(20000, True, True, True, 0)
print(result)


#RETURN AND PRINT:
def add_print(a, b):
    print(a + b)

def add_return(a, b):
    return a + b

x = add_print(2,3)
y = add_return(2,3)


##EXERCISE NUMBER FIRST()

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
