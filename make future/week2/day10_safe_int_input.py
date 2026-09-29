#making loop
def safe_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

#Usage eample:
number = safe_int_input('Enter a number: ')
print(f'You entered: {number}')


