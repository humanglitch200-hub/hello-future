print(" ==================='Interactive Bill Splitter'=================== ")
print("  ")
print("  ")
print("  ")
try:
   bill_amt = float(input("Enter you total bill amount: "))
   tip = float(input("what percentage of tip you gave: "))

except: 
   print("Enter valid numer , man!")

print(bill_amt)
print(f"{tip}%")
numberofppl = float(input("Enter number of people on resturant: "))

print(" --- Billa Summarry --")
tipamount = tip / bill_amt
print(tipamount)


total = tipamount + bill_amt
print(f"Total money tip + bill = {total:.2f}")

perperson_share = total / numberofppl
print(f"{perperson_share:.2f}")
