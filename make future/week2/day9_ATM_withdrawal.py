#asking
while True:
    balance = int(input("Enter your balance: "))
    withdrawl_amount = int(input("Withdrawal amount: "))
    if withdrawl_amount <= 0:
         print('please enter valid amount! ')

    about_card = input("card is active(y/n): ")

#Rules
    if about_card == 'n':
       print("Your card is blocked!")

    elif withdrawl_amount > balance:
        print("Insufficient funds.")

#Trying somehting
    elif withdrawl_amount > 1000:
        print("Daily limit exceeded!")

        tryy = input("Do you want to retry? (yes/no)")
        if tryy !='yes':
            break
