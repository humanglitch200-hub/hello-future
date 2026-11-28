#part A
n = int(input("number: "))
print("got:", n)

#part B
def ask_int(message):
    while True:
        raw =input(message)
        try:
            return int(raw)
        except ValueError:
            print("not a number")

n = ask_int("number: ")
print("got: ",n)

def ask_yes_no(message):
    while True:
        answer = str(input(message)).strip().lower()
        if answer in ('y', 'n'):
                return answer in ('y', )
        
        print("Please type 'y' or  n ")

mew = ask_yes_no("continue: ")
print("got: ",mew)