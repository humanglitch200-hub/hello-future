# Ask: item name, quantity, and if customer is a member
# Rules:
#   - Empty item name → "Please enter an item"
#   - quantity <= 0 → "Invalid quantity"
#   - Otherwise:
#       - quantity >= 5 AND member → "Bulk + member discount applied"
#       - quantity >= 5 → "Bulk discount applied"
#       - member → "Member discount applied"
#       - else → "No discount"


#Makinf lists, asking the user with some rules:
item = input("Item name: ")
if item =='':
    print("Please enter an item: ")

    
quantity = int(input("quantity: "))
if quantity <= 0:
    print("Invaild quantity")

member = input("Are you member (y/n): ")
discount = []
#making rules
if quantity >= 5 and member == 'y':
    discount = 'Bulk + member discout applied'

elif quantity >= 5:
    discount = 'Bulk discount applied.'

elif member == 'y':
    discount = 'Member discount applied'

else:
    discount = 'No discount'

print(f'you bought {quantity}kg {item}.')
print(f'{discount}')