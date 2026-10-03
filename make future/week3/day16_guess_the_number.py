import random
guesses_try = 0
secret = random.randint(1,101)
while True:
    try:
        guess = int(input("Guess the number (1-100): "))
        if guess <1 or guess > 100:
            print("Please enter a number between 1-100.")
            continue

        guesses_try += 1      #keeping the histry to show!

        if guess == secret:
            print(f"Correct! You got it in {guesses_try} tries")

        elif guess >= secret:
            print("Too high")

        else:
            print("Too low")
    except ValueError:
        print("Please enter a number. ")

 
    


