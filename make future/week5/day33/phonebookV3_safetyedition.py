import os
contacts = []

def backup_file(filename):
    if not os.path.exists(filename):
        return None
    with open(filename, 'r', encoding = 'utf-8') as f:
        content = f.read()
    with open(filename+'.bak', 'w', encoding = 'utf-8') as f:
        f.write(content)

def restore_from_backup(filename):
    if not os.path.exists(filename +'.bak'):
        print("backup not available")
        return False
    with open(filename + '.bak','r', encoding ='utf-8') as f:
        content = f.read()
    with open(filename, 'w', encoding = 'utf-8') as f:
        f.write(content)
    return True

def load(filename):
    contacts.clear()
    if not os.path.exists(filename):
        if os.path.exists(filename + '.bak'):
            restore_from_backup(filename)
            print("Recovered from backup")   
        else:
            return None              
    if os.path.exists(filename):
        with open(filename, 'r', encoding = 'utf-8') as f:
            for l in f:
                l = l.strip()
                if not l:
                    continue
                parts = l.split("|")
                if len(parts) != 2:
                    continue
                contacts.append({"name": parts[0], "phone": parts[1]})
    return contacts  

def save(filename, contacts):
    backup_file(filename)
    if os.path.exists(filename):
        with open(filename, 'w', encoding = 'utf-8') as f:
            for c in contacts:
                f.write(f"{c['name']}|{c['phone']}\n")

def add(name, phone):
    contacts.append({"name": name, "phone": phone})
    return contacts

def search(find):
    result = []
    for c in contacts:
        if find.lower() in c['name'].lower() or find in c['phone']:
            result.append(c)
    return result

def edit(index, new_phone):
    contacts[index]['phone'] = new_phone
    return True

def delete(index):
    del contacts[index]
    return True

if __name__ =="__main__":
    load("week5/day33/phonebook.txt")
    if contacts:
        print(f"loaded {len(contacts)} contacts.")
    else:
        print("nothing to load.\nstarting fresh.")
    while True:
        print()
        print("1. Add")
        print("2. View")
        print("3. Search")
        print("4. Edit")
        print("5. Delete")
        print("6. Quit")

        try:
            choice = int(input("choice: "))
        except ValueError:
            print("unvalid choice.")
            continue

        if choice == 1:
            name = input("name: ")
            phone = input("phone: ")
            add(name,phone)
            save("week5/day33/phonebook.txt", contacts)

        elif choice == 2:
            for c in contacts:
                print(f"{c['name']}= {c['phone']}")

        elif choice == 3:
            find = input("search: ")
            catch = search(find)
            if catch:
                for c in catch:
                    print(f"{c['name']}: {c['phone']}")
            else:
                print("no match")

        elif choice == 4:
            if not contacts:
                print("nothing on file")
                continue
            for i, c in enumerate(contacts, 1):
                print(f"{i}. {c['name']}= {c['phone']}")
            try:
                i = int(input("index: "))
                index = i -1
                if index >= len(contacts) or index < 0:
                    print("enter valid index.")
                    continue
            except ValueError:
                print("invalid index")
                continue
            new_phone = input("new number: ")
            
            if edit(index, new_phone):
                print("number edited.")
            save("week5/day33/phonebook.txt",contacts)

        elif choice == 5:
            if not contacts:
                print("nothing to delete")
                continue
            for i,c in enumerate(contacts, 1):
                print(f"{i}. {c['name']}: {c['phone']}")
            try:
                i = int(input("index: "))
                index = i -1
                if index >= len(contacts) or index < 0:
                    print("invalid index")
                    continue
            except ValueError:
                print("invalid input!")
                continue

            if delete(index):
                print("contact removed.")
            save("week5/day33/phonebook.txt",contacts)

        elif choice == 6:
            print("see you.")
            break

        else:
            print("enter valid choice")
            continue
                    

 


            


            

        





