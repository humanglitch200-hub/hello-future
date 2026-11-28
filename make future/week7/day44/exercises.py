def ask_int(message, lo, hi):
    while True:
        try:
            value = int(input(message))
                
        except ValueError:
            print("Invalid input. Try again!")
            continue

        if lo <= value <= hi:
            return value
        print(f"must be {lo}..{hi}")

def safe_int(value, default= None):
    try:
        return int(value)
    except ValueError:
        return default

def ask_choice(message, valid_choices):
    while True:
        choice = input(message).strip().lower()
        if choice in valid_choices:
            return choice
        
print(ask_int("enter: ", 100, 1000))
print(safe_int('sav'))
VALIDS = ['mew', 'lower']
print(ask_choice("Enter: ", VALIDS))