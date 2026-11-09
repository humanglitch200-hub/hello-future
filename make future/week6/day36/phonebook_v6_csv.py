import csv
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PHONEBOOK_FILE = os.path.join(BASE_DIR, 'phonebook.csv')
BACKUP_FILE = os.path.join(BASE_DIR, 'phonebook.csv.bak')

def load(contacts, filename):
    if not os.path.exists(filename):
        return contacts
    with open(filename, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for l in reader:
            if len(l) < 2:
                continue
            contacts.append({"name": l[0],  "phone": l[1]})
    return contacts

def save(contacts, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        for c in contacts: 
            writer.writerow([c['name'], c['phone']])

def search(contacts, find):
    result = []
    for c in contacts:
        if find in c['name']or find in c['phone']:
            result.append(c)
    return result

def edit(contacts, index, new_phone):
    contacts[index]['phone']=new_phone
    return contacts

def view(contacts):
    for c in contacts:
        print(f"Name: {c['name']} | Phone: {c['phone']}")

def add(contacts, name, phone):
    contacts.append({"name": name, "phone": phone})

def delete(contacts, index):
    del contacts[index]

def main():
    contacts = []
    contacts = load(contacts, PHONEBOOK_FILE)
    if contacts:
        print(f"loaded {len(contacts)} contacts.")
    else:
        print("Starting fresh.")

    while True:
        print()
        print("1. Add")
        print("2. View")
        print("3. Edit")
        print("4. Delete")
        print("5. Search")
        print("6. Save")
        print("7. Quit")
        try:
            choice = int(input("Choice: "))
        except ValueError:
            print("invalid choice.")
            continue

        if choice == 1:
            name = input("Name: ")
            phone = input("Phone: ")
            add(contacts, name, phone)
            print("added.")

        elif choice == 2:
            if not contacts:
                print("nothing on the list.")
                continue
            view(contacts)

        elif choice == 3:
            if not contacts:
                print("nothing to edit.")
                continue
            for i, c in enumerate(contacts, 1):
                if len(c) < 2:
                    continue
                print(f"{i}. {c['name']} | {c['phone']}")
            try: 
                index = int(input("Index: ")) -1
                if index < 0 or index >= len(contacts) :
                    print("invalid choice.")
                    continue
            except ValueError:
                print("invalid keyword")
                continue

            new_phone = input("New phone: ")
            edit(contacts,index, new_phone)

        elif choice == 4:
            if not contacts:
                print("Nothing to delete.")
                continue
            for i, c in enumerate(contacts,1):
                if len(c) < 2:
                    continue 
                print(f"{i}. {c['name']} | {c['phone']}")
            try: 
                index = int(input("index: "))-1
                if index <= 0 or index >= len(contacts):
                    print("invalid index")
                    continue
            except ValueError:
                print("invalid keyword!")
                continue

            delete(contacts, index)
            print("deleted.")
    
        elif choice == 5:
            find = input("Search: ")
            result = search(contacts, find)
            if result:
                for c in result:
                    print(f"Name: {c['name']} | Phone: {c['phone']}")
            else:
                print('no match')

        elif choice == 6:
            save(contacts, PHONEBOOK_FILE)
            print("Saved.")

        elif choice == 7:
            print("Bye.")
            break

        else:
            print("enter valid choice.")
            continue
    
if __name__ == "__main__":
    main()
