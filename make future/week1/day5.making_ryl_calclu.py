# --- Before the loop ---
history = []

while True:
    # --- Step 1: Get first number, check for 'q' ---
    first_input = input("Enter first number (or 'q' to quit): ")

    if first_input == 'q':
        break

    # --- Step 2: Check for 'history' ---
    if first_input == 'history':
        if history:
            print("\n--- History ---")
            for item in history:
                print(item)
            print("---------------\n")
        else:
            print("No history yet.")
        continue

    # --- Step 3: Convert to float, catch errors ---
    try:
        first = float(first_input)
    except ValueError:
        print("That's not a number!")
        continue

    # --- Step 4: Get second number ---
    second_input = input("Enter second number: ")
    try:
        second = float(second_input)
    except ValueError:
        print("That's not a number!")
        continue

    # --- Step 5: Get operation ---
    operation = input("Enter operation (+, -, *, /, %, **): ")

    # --- Step 6: Do the math ---
    if operation == '+':
        result = first + second
    elif operation == '-':
        result = first - second
    elif operation == '*':
        result = first * second
    elif operation == '/':
        if second == 0:
            print("Error: cannot divide by zero")
            continue
        result = first / second
    elif operation == '%':
        if second == 0:
            print("Error: cannot divide by zero")
            continue
        result = first % second
    elif operation == '**':
        result = first ** second
    else:
        print("Invalid operation!")
        continue

    # --- Step 7: Show result + save to history ---
    print(f"{first} {operation} {second} = {result}")
    history.append(f"{first} {operation} {second} = {result}")

    # --- Step 8: Ask to continue ---
    continue_choice = input("Do you want to continue? (y/n): ")
    if continue_choice != 'y':
        break

print("Goodbye!")   