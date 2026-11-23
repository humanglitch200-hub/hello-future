import os, json
DATA_FILE = os.path.dirname(os.path.abspath(__file__))
BASE_FILE = os.path.join(DATA_FILE, 'phonebok_v10.json')
FIELDS = ['name', 'phone']

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
            return (False, f"bad or missing field: {field}")
    return (True, None)

def load(contacts, filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if not isinstance(data, list): 
                return contacts
            clean = []
            for row in data:
                valid, _ = is_valid_row(row, FIELDS)
                if valid:
                    clean.append(clean_row(row, FIELDS))
            return clean
    except FileNotFoundError:
        return contacts
    except json.JSONDecodeError:
        return contacts

def save(contacts, filename):
    with open(filename, 'w', encoding = 'utf-8') as f:
        json.dump(contacts, f, indent=2, ensure_ascii=False)

def add(contacts, name, phone):
    row = {"name": name, "phone": phone}
    ok, reason = is_valid_row(row, FIELDS)
    if not ok:
        print(f"Bad: {reason}")
        return False
    contacts.append(clean_row(row, FIELDS))
    return True

def search(contacts, keyword):
    keyowrd = keyword.lower()
    result = []
    for c in contacts:
        if keyword in c['name'] or keyword in c['phone']:
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
    contacts = []
    contacts = load(contacts, BASE_FILE)
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
                save(contacts, BASE_FILE)

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
            save(contacts, BASE_FILE)

        elif choice == 3:
            save(contacts, BASE_FILE)
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
            save(contacts, BASE_FILE)

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
