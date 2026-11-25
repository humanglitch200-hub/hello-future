import os, json

DATA_FILE = os.path.dirname(os.path.abspath(__file__))
BASE_FILE = os.path.join(DATA_FILE, "phonebook_v11_wrapped.json")
FIELDS = ['name','phone']

def load():
    try:
        with open(BASE_FILE, 'r', encoding='utf-8') as f:
            contacts = json.load(f)
        if isinstance(contacts, list):
            print(f"\nLegacy file detected - will save as wrapped on next write.")
            return contacts
        else:
            data_list= contacts.get("contacts",[])
            return data_list
        
    except FileNotFoundError:
        print("file doesn't exists. making new!")
        return []
    except json.JSONDecodeError as e:
        print(f"Decode Error: {e}")
        return []

def save(contacts):
    payload = {"version": 1, "contacts": contacts}
    with open(BASE_FILE, 'w', encoding='utf-8') as f:
        json.dump(payload, f, indent=2, ensure_ascii=False, sort_keys=True)

def clean_row(row, fields):
    clean = {}
    for field in fields:
        value = row.get(field, "")
        if value is None:
            value = ""
        clean[field] = str(value).strip()
    return clean

def is_duplicate(contacts, name):
    for c in contacts:
        if c['name'].lower() == name.lower():
            return True
    return False

def is_valid_row(row, required_fields):
    for field in required_fields:
        if not field in row or not isinstance(row[field], str) or not row[field].strip():
            return (False, f"Bad or missing field: {field}")
    return (True, None) 

def add(contacts, name, phone):
    row = {"name": name, "phone": phone}
    ok, reason = is_valid_row(row, FIELDS)
    if not ok:
        print(f"Bad: {reason}")
        return False
    contacts.append(clean_row(row, FIELDS))
    return True

def search(contacts, keyword):
    result = []
    for c in contacts:
        if keyword in c['name'].lower() or keyword in c['phone'].lower():
            result.append(c)
    return result

def edit(contacts, index, new_phone):
    contacts[index]['phone'] = new_phone

def delete(contacts, index):
    del contacts[index]

def view(contacts):
    for c in contacts:
        print(f"Name: {c['name']} | Phone: {c['phone']}")

def main():
    contacts = load()
    if not contacts:
        print("starting fresh.")
    else:
        print(f"loaded {len(contacts)} contacts.")


    while True:
        print()
        print("1. Add")
        print("2. Edit")
        print("3. Save")
        print("4. Delete")
        print("5. Search")
        print("6. View")
        print("7. Quit")

        try:
            choice = int(input("choice: "))
        except ValueError:
            print("invalid choice")
            continue

        if choice == 1:
            name = input("Name: ")
            phone = input("Phone: ")

            duplicate = is_duplicate(contacts, name)    
            if duplicate:
                answer = input(f"the given name({name}) already exists. Though do you want to save(y/n): ")
                if answer not in('y', 'yes', 'Y', 'YES'):
                    continue
                
            if add(contacts, name, phone):
                print("contact added.")
                save(contacts)

        elif choice == 2:
            for i, c in enumerate(contacts, 1):
                print(f"{i}. {c['name']}: {c['phone']}")

            try:
                index = int(input("index: ")) - 1
                if index < 0 or index >= len(contacts):
                    print("invalid index given.")
                    continue
            except ValueError:
                print("enter index!")
                continue

            new_phone = input("New phone: ")
            edit(contacts, index, new_phone)
            print("contact edited")
            save(contacts)

        elif choice == 3:
            save(contacts)
            print("contacts saved.")

        elif choice == 4:
            for i, c in enumerate(contacts, 1):
                print(f"{i}. {c['name']}: {c['phone']}")
            
            try:
                index = int(input("index: ")) - 1
                if index < 0 or index >= len(contacts):
                    print("invalid index!")
                    continue
            except ValueError:
                print("enter index!")
                continue

            delete(contacts, index)
            save(contacts)

        elif choice == 5:
            if not contacts:
                print("nothing to search")
                continue

            keyword = input("search: ").lower()
            result = search(contacts, keyword)
            if not result:
                print("no match")
                continue
            else:
                for c in result:
                    print(f"{c['name']}: {c['phone']}")

        elif choice == 6:
            view(contacts)

        elif choice == 7:
            break

        else:
            print("enter (1-7) !!")
            continue

if __name__ == "__main__":
    main()


