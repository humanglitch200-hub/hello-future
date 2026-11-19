import os, csv
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'phonebook_v8.csv')
FIELDS = ["name", "phone"]

def is_valid_row(row, required_fields):
    for field in required_fields:
        if field not in row or row[field] is None:
            return(False, f"missing field: {field}")
    for field in required_fields:
        if not row[field].strip():
            return(False, f"empty field: {field}")
    if None in row:
        return (False, "extra columns")
    return (True, None)

def load(contacts, filename):
    if not os.path.exists(filename):
        print("No data file found.")
        return contacts
    with open(filename, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            ok, reason = is_valid_row(row, FIELDS)
            if ok:
                contacts.append({"name": row['name'], "phone": row['phone']})
            else:
                print(f"Warning: skipping bad row ({reason}): {row}")
                continue
        return contacts

def save(contacts, filename):
    with open(filename, 'w', newline='', encoding='utf-8')as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        writer.writerows(contacts)

def add(contacts, name, phone):
    contacts.append({"name": name, "phone": phone})

def view(contacts):
    for c in contacts:
        print(f"Name: {c['name']} | Phone: {c['phone']}")

def edit(contacts, index, new_phone):
    contacts[index]['phone'] = new_phone

def delete(contacts, index):
    del contacts[index]

def search(contacts, keyword):
    result =[]
    for c in contacts:
        if keyword in c['name'] or keyword in c["phone"]:
            result.append(c)
    return result

def main():
    contacts = []
    contacts = load(contacts, DATA_FILE)
    if contacts:
        print(f"load {len(contacts)} contacts.")
    else:
        print("starting fresh")
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
            add(contacts, name, phone)
            save(contacts, DATA_FILE)

        elif choice == 2:
            if not contacts:
                print("--- just started ---")
                continue
            view(contacts)

        elif choice == 3:
            if not contacts:
                print("Nothing to show.")
                continue
            for i, c in enumerate(contacts, 1):
                print(f"{i}. {c['name']}: {c['phone']}")
            index = int(input("index: ")) -1
            if index <0 or index >= len(contacts):
                print("invalid index!")
                continue
            new_phone= input("new phone: ")
            edit(contacts, index, new_phone)
            save(contacts, DATA_FILE)

        elif choice == 4:
            if not contacts:
                print("nothing to edit")
                continue
            for i,c in enumerate(contacts, 1):
                print(f"{i}. {c['name']}: {c['phone']}")
            index = int(input("index: ")) - 1
            if index < 0 or index >= len(contacts):
                print("invalid index!")
                continue
            delete(contacts, index)
            save(contacts, DATA_FILE)

        elif choice == 5:
            if not contacts:
                print("nothing to search!")
                continue
            keyword = input("find: ")
            result = search(contacts, keyword)
            if result:
                for c in result:
                    print(f"{c['name']}: {c['phone']}")
            else:
                print("nothing found!")

        elif choice == 6:
            if not contacts:
                print("nothing to save")
            else:
                save(contacts, DATA_FILE)
                print(f"{len(contacts)} contact saved")

        elif choice == 7:
            print("see you.")
            break

        else:
            print("invalid choice. Enter(1-7)")
            continue

if __name__ == "__main__":
    main()




        



    

