###Option C — Personal Budget Planner
#Ask income, then expenses
#Categorize (food, transport, rent, fun)
#Report: how much left, overspending warning
#Uses functions, nested conditions, truthy/falsy


#Input validation wrapper:
def safe_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('Please input valid number!')

#Taking input from user
def get_expenses():
    expenses = {}
    expenses["food"]      = safe_float("Food: ")
    expenses["transport"] = safe_float("Transport: ")
    expenses["rent"]      = safe_float("Rent: ")
    expenses["fun"]       = safe_float("Fun: ")
    expenses["education"] = safe_float("Education: ")
    return expenses

#Budget analyzer :
def analyze_budget(income, expenses):
    total_expenses = sum(expenses.values())
    remaining = income - total_expenses

    if remaining < 0:

        #Finding biggest:
        biggest = max(expenses, key=expenses.get)

        return f"⚠️ Overspent by {abs(remaining):.2f}. Biggest drain: {biggest}"
    
    elif remaining == 0:
        return "You broke even."
    
    elif remaining < income * 0.3:
        return f"okay, but watch it. {remaining:.2f} remaining."
    
    else:
        return f"Great! You saved {remaining:.2f} this month."

#Printing all the things with summary:
def main():
    print("=== Personal Budget Planner ==\n")
    while True:

        while True:
                income = safe_float("Monthly income: ")
                if income > 0:
                     break
                print('Income must be grater than 0. Try again! ')
                    
                 
        # if income <= 0:
        #     print("please Enter a valid number! ")
        
        expenses = get_expenses()
        total_spent = sum(get_expenses.values())

        report = analyze_budget(income, expenses)
        print(f"\n{report}")

        # total = sum(expenses.values())
        print("\n ---summary ---")
        print(f"Income:     {income:.2f}")
        print(f"Spent:      {total_spent}")

        remaining = income - total_spent
        print(f"Remaining:  {remaining:.2f}")
        print("-" * 20)      

#Printing what percentage of income each thing spent on what:
        for category, amount in expenses.items():
            pct = (amount / income) * 100
            print(f"{category:<10} {pct:.0f}%")

        again = input("\nCalculate again? (yes/no): ").lower()
        if not again.startswith("y"):
            break

    print("Goodbye!")

#Don't know but according to deepseek it is imprtant:
if __name__ == "__main__":
    main()



