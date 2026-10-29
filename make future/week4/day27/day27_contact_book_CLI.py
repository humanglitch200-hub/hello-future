contacts = {}
#pb350024@gmail.com
def add(name, phone, email):
    if not name:
        return None
    if not name in contacts.keys():
            contacts[name] = {"phone": phone, "email": email}
            return True
    else:
        return False


def find(name):
    if not name:
        return None
    if name in contacts.keys():
         return contacts[name]
    return None

def delete(name):
    if not name:
        return None
    if name in contacts:
        contacts.pop(name)
        return True
    return False

def list_all():
    if not contacts:
        return None
    for name, info in contacts.items():
        print(f"{name}\nPhone: {info["phone"]}\nEmail: {info["email"]}")

def search(term):
    if not term:
        return None
    result = []
    for name, info in contacts.items():
        if term in info["email"] or term in name:
            result.append(name) 
 
    return result

while True:
    if __name__ == "__main__":
        print()
        print('=== Contact Book ===')
        print('1. Add contact')
        print('2. Find contact')
        print('3. Delete contact')
        print('4. List all')
        print('5. Search')
        print('6. Quit')

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please Enter Number!")
            continue

        if choice == 1:
            try:
                name = input("Name: ").lower().strip()
            except ValueError:
                print('Enter name!')
                continue
            try:
                phone = int(input("Phone: "))
            except ValueError:
                print("Enter phone number!")   
                continue
            email = input("Email: ").lower()
            if not email.endswith('@gmail.com'):
                print('Enter Valid Email!')
                continue 
            if add(name, phone, email):      
                print(f'✓ Added {name}.')
            else: 
                print(f'Name already exists: {name}.')
            
        elif choice == 2:
            try: 
                name = input("Name: ").strip()
            except ValueError:
                print('Enter name!')
                continue
            print('Searching...')
            find(name)
            found = False
            for k, v in contacts.items():
               if name == k:
                    print(f"{k} — {v}")
                    found = True
               if not found:
                    print("Contact not found.")
            
        elif choice == 3:
            try:
                name = input('Name of contact to delete: ')
            except ValueError:
                print("Enter name!")
                continue
            delete(name)
            if name in contacts.keys():
                print('Contact of',name,'Deleted..')
            else:
                print(f"Contact not found({name})...")
            

        elif choice == 4:
            if not contacts:
                print("Nothing on the list...")
            list_all()

        elif choice == 5:
            term = input("Seacrh by email or name: ")
            print('searching...') 
            search(term)
            for name, info in contacts.items():
                if term in name or term in info["email"]:
                    print(search(term))
                    print(f'Phone= {info["phone"]},  Email= {info["email"]} ')
                else: 
                   print("nothing found")
            
        elif choice == 6:
            print("Bye...")
            break

        else:
            print('Enter number (1-6).')
            continue
            
            

            


            


    