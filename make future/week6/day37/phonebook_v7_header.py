import os
import csv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'phonebook_v7.csv')
FIELDS = ["name", "phone"]
contacts = []

def load(contacts, filename):
    if not os.path.exists(filename):
        print("file not found.")
        return []
    with open(filename, 'r', newline='', encoding= 'utf-8')as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['name'] is None or row['name'] =='' or row['phone'] is None or row['phone'] =='':
                continue
            contacts.append({"name": row['name'], "phone": row['phone']})
        return contacts


def save(contacts, filename):
    with open(filename, 'w', newline='', encoding= 'utf-8')as f:
        fieldnames = FIELDS
        writer = csv.DictWriter(f, fieldnames=fieldnames)         

        writer.writeheader()
        writer.writerows(contacts) 

def add(contacts, name, phone):
    contacts.append({"name": name, "phone": phone})

def view(contacts):
    for row in contacts:
        print(f"Name: {row['name']} | Phone: {row['phone']}")

def edit(contacts, index, new_phone):
    contacts[index]['phone'] = new_phone

def delete(contacts, index):
    del contacts[index]

def search(contacts, keyword):
    result = []
    for row in contacts:
        if keyword in row['name'] or keyword in row['phone']:
            result.append(row)
    return result

def main():
    contacts = []
    contacts = load(contacts, DATA_FILE)
    if contacts:
        print(f"loaded {len(contacts)} file")
    else:
        print('starting fresh')
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
            choice = int(input("choice: "))
        except ValueError:
            print("invalid choice.")
            continue
        if choice == 1:
            name = input("Name: ")
            phone = input("Phone: ")
            if name =='' or phone =='':
                print("invalid input given.")
                continue
            add(contacts, name, phone)
            save(contacts, DATA_FILE)

        elif choice == 2:
            if not contacts:
                print("nothing found.")
                continue
            view(contacts)
        
        elif choice == 3:
            for i, row in enumerate(contacts, 1):
                print(f"{i}. Name: {row['name']} | Phone: {row['phone']}")
            try:
                index = int(input("index: "))-1
                if index < 0 or index >= len(contacts):
                    print("invalid index.")
                    continue
            except ValueError:
                print("provide index.")
                continue
            new_phone = input("new phone: ")

            edit(contacts, index, new_phone)
            save(contacts, DATA_FILE)
        
        elif choice == 4:
            for i, row in enumerate(contacts, 1):
                print(f"{i}. Name: {row['name']} | Phone: {row['phone']}")
            
            try:
                index = int(input("index: ")) - 1
                if index < 0 or index >= len(contacts):
                    print("invalid index.")
                    continue
            except ValueError:
                print("enter index.")
                continue
            delete(contacts, index)
            save(contacts, DATA_FILE)

        elif choice == 5:
            keyword = input("search: ")
            result = search(contacts, keyword)
            if result: 
                for row in result:
                    print(f"Name: {row['name']}, Phone: {row['phone']}")
            else:
                print("nothing found")

        elif choice == 6:
            if not contacts:
                print("nothing to save")
                continue
            save(contacts, DATA_FILE)
            print('contacts saved...')

        elif choice == 7:
            print('bye')
            break

        else:
            print("choice must be (1-7)")
            continue

if __name__ == "__main__":
    main()




                




