member = input("Are you member of pb.co (y/n)? ")
#ASKING FOR THE PURCHASE AMOUNT
amount = int(input("Wht's your total purchase amount: "))

Discount = []
#APLTING DISCOUNT
if amount >= 1000 and member =='y':
    Discount = 20 * amount / 100
elif amount >= 1000 and member =='n':
    Discount = 10 * amount / 100
elif amount >= 500:
    Discount = 5 * amount / 100
else: Discount = 0

total = amount - Discount
print("discount prize:", Discount)
print("Total Bill amount is: ",total )