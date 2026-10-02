#Safety rule for input
def safe_float(prompt):
    while True:
        try:
            return float(input(prompt))

        except ValueError:
            print ("Please Enter float Number! ")

#Total list of expenses:
def get_expenses():
    expenses = {}
    expenses["food"]           = safe_float("Food: ")
    expenses["transportation"] = safe_float("Transportation: ")
    expenses["fun"]            = safe_float("Fun: ")
    expenses["education"]      = safe_float("education: ")
    return expenses

#Bugdet Analyzer ,  Finding Rmaining and Biggest Leak:
def budget_analyze(income, expenses):
    total_expenses = sum(expenses.values())
    remaining = income - total_expenses
    biggest = max(expenses, key=expenses.get)


#looping the remaining for the result:
    if remaining < 0:
        return f"Over spent on: {abs(remaining):.2f}. Biggest drain on: {biggest}", remaining, total_expenses
    elif remaining == 0:
        return "You are broke even!", remaining, total_expenses
    elif remaining < income * 0.3:
        return f"Nice, But watch it, Remaining: {remaining:.2f}/-", remaining, total_expenses
    else:
        return f"Great you saved: {remaining:.2f} this month.", remaining, total_expenses
 

#Printing  visuals, and looping:
def main():
    print("====Budget analyzer===")
    while True:
        while True:            
            income = safe_float("Enter your monthly income: ")
            if income >= 1:                   
                break
            print ("Income must be grater than 0. Try again.")

        expenses = get_expenses()
        report, remaining, total_spent = budget_analyze(income, expenses)

        #printing summary:
        print(f"\n{report}")
        print(f"Income:         {income}")
        print(f"Total Spent:    {total_spent}")
        print(f"Remain Balance: {remaining}")
        print("-" * 20)



        for category, amount in expenses.items():
            pct = (amount / income) * 100
            print(f"{category:<10} {pct:.0f}%")

        again = input("Do you want to retry? (yes/no): ")
        if not again.startswith("y"):
            break

    print("See You!")

if __name__ == "__main__":
    main()




    
    



        