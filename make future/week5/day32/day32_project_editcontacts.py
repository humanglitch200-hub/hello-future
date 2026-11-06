contacts = []
def load(filename):
    try:
        contacts.clear()
        with open(filename, 'r', encoding = 'utf-8') as f:
            for l in f:
                l = l.strip()
                if not l:
                    continue
                parts = l.split(" | ")
                if len(parts) != 2:
                    continue
                contacts.append({"name": parts[0], "phone": parts[1]})
        
    except FileNotFoundError:
        return None
    return contacts

def save(filename, contacts):
    if not filename: return None
    with open (filename, 'w', encoding = 'utf-8') as f:
        for c in contacts:
            f.write(f"{c['name']} | {c['phone']}\n")

def add(name, phone):
    contacts.append({"name": name, "phone": phone})
    return contacts

def search(search):
    result =[]
    for c in contacts:
        if search in c['name'] or search in c['phone']:
            result.append(c)
    return result

def edit(index, new_phone):
     contacts[index]["phone"] = new_phone

def delete(index):
    del contacts[index]
    

if __name__ == "__main__":
    load('contactshub.txt')
    if contacts:
        print(f"{len(contacts)} contacts loaded.")
    else:
        print("Nothing to load. Starting fresh!")

    while True:
        print()
        print("1. Add  contact")
        print("2. Edit contact")
        print("3. Find contacts")
        print("4. Delete contact")
        print("5. Quit")

        try:
            choice = int(input("Choice: "))
        except ValueError:
            print('enter valid number!')
            continue

        if choice == 1:
            name = input("Name: ")
            phone = input("Number: ")
            add(name, phone)
            save('contactshub.txt', contacts)
            print("contact added.")

        elif choice == 2:
            for i, c in enumerate(contacts, 1):
                print(f"{i}. {c['name']}: {c['phone']}")

            try:
                i = int(input("Edit which: "))
                index = i-1
                if index < 0 or index > len(contacts):
                    print("unvalid index provided.")
                    continue
            except ValueError:
                print("Enter index!")
                continue
            new_phone = input("New phone: ")
            for c in contacts:
                if str(new_phone) == c['phone']:
                    print("Same number found with another name: ")
                    print(f"Name:  {c['name']}")
                    print(f"Phone: {c['phone']}")
            edit(index, new_phone)
            save('contactshub.txt', contacts)

        elif choice == 3:
            find = input("Search: ")
            result = search(find)
            if result:
                for c in result:
                    print(f"Name:  {c['name']}")
                    print(f"Phone: {c['phone']}")
                    print()
            else:
                print("no match")

        elif choice == 4:
            if not contacts:
                print("nothing to delete.")
                continue
            else:
                for i, c in enumerate(contacts, 1):
                    print(f"{i}. {c['name']}- {c['phone']}")

                try:
                    wipe = int(input("Index: "))
                    index = wipe -1
                    if index < 0 or index > len(contacts):
                        print("out of range.")
                        continue

                except ValueError:
                    print("provide number.")
                    continue

                delete(index)
                save('contactshub.txt', contacts)

        elif choice == 5:
            print('see you')
            save('contactshub.txt', contacts)
            break

        else:
            print("provide number(1-5)!")
            continue






        





