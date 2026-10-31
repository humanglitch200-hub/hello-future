contacts = []
def load(filename):
    try:
        with open(filename, 'r', encoding= 'utf-8') as f:
            for line in f:
               line = line.strip()
               if not line:
                   continue
               name, phone = line.split('|')
               contacts.append({"name": name, "phone": phone})
    except FileNotFoundError:
        pass
    return contacts

def save(filename, contacts):
    with open(filename, 'w', encoding = 'utf-8') as f:
        for c in contacts:
            f.write(f'{c["name"]} | {c["phone"]}\n')

def add(contacts, name, phone):
    contacts.append({"name": name, "phone": phone})
    return contacts

def view(contacts):
    for i, c in enumerate(contacts ):
            print(f"{i}. {c}")




if __name__ == "__main__":
    contacts = load('phonebook.txt')
    if contacts:
        print(f"Loaded {len(contacts)} contacts.")
    else:
        print("NO file yet. starting fresh.")

    while True:
        print()
        print("1. Add contact")
        print("2. View all")
        print("3. Save to file")
        print("4. Quit")

        try:
            choice = int(input("Choice = "))
        except ValueError:
            print("Enter valid choide...")
            continue

        if choice == 1:
            name = input("name: ")
            try:
                phone = int(input("number: "))
            except ValueError:
                print("Enter Valid number...")
                continue
            
            add(contacts, name, phone)
            print("added..")

        elif choice == 2:
            if not contacts:
                print("Nothing found...")
            else:
                view(contacts)

        elif choice == 3:
            print('saving to the file...')
            if not contacts:
                print("nothing to save")
            else:
                save('phonebook.txt', contacts)
                print("saved successfully.")

        elif choice == 4:
            save('phonebook.txt', contacts)
            print('see you...')
            break

        else:
            print("Enter choice(1-4): ")



        
        
