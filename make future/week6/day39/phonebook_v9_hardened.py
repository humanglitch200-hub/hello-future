import os, csv
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, 'phonebook_v9.csv')
FIELDS = ['name', 'phone']


def is_valid_row(row, required_fields):
    for field in required_fields:
        if field not in row or row[field] is None:
            return (False, f"missing field: {field}")

    for field in required_fields:
        if not row[field].strip():
            return(False, f"bad feild")

    if None in row:
        return (False, "extra columns")
    return (True, None)

def is_duplicate(contacts, name):
    for c in contacts:
        if c['name'].lower() == name.lower():
            return True
    return False

def clean_row(row, fields):
    clean = {}
    for field in fields:
        value = row.get(field, "")
        if value is None:
            value = ""
        clean[field] = str(value).strip()
    return clean

def load(contacts, filename):
    if not os.path.exists(filename):
        return contacts
    with open(filename, 'r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f, skipinitialspace = True)
        if reader.fieldnames != FIELDS:
            print(f"Warning: header is{reader.fieldnames} excepted{FIELDS}")
            reader.fieldnames = [name.strip().lower() for name in reader.fieldnames]

        for row in reader:
            ok, reason = is_valid_row(row, FIELDS)
            if ok:
                contacts.append(clean_row(row, FIELDS))
            else:
                print(f"skipped row: {row} because {reason}")
        return contacts

def save (contacts, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, quoting=csv.QUOTE_ALL, restval='', extrasaction='ignore')
        writer.writeheader()
        writer.writerows(contacts)

def add(contacts, name, phone):
        contacts.append({"name": name, "phone": phone})

def edit(contacts, index, new_phone):
    contacts[index]['phone'] = new_phone

def delete(contacts, index):
    del contacts[index]

def search(contacts, keyword):
    result = []
    for c in contacts:
        if keyword in c['name'] or keyword in c['phone']:
            result.append(c)
    return result 

def view(contacts):
    for c in contacts:
        print(f"Name: {c['name']}, phone: {c['phone']}")

def main():
    contacts = []
    contacts = load(contacts, DATA_FILE)
    if not contacts:
        print("Starting fresh")
    else:
        print(f"loaded {len(contacts)} contacts.")

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

            duplicate = is_duplicate(contacts, name)
            if duplicate:
                answer = input(f"Given name ({name}) already exists. Add anyway? (y/n): ")
                if answer not in ('y', 'yes'):
                    print("contact NOT added.")
                    continue
           
            add(contacts, name, phone)
            print("contact added.")
            save(contacts, DATA_FILE)

        elif choice == 2:
            if not contacts:
                print("Nothing to watch.")
                continue

            view(contacts)

        elif choice == 3:
            for i, c in enumerate(contacts, 1):
                print(f"{i}. {c['name']}: {c['phone']}")

            index = int(input("index: ")) - 1
            if index < 0 or index >= len(contacts):
                print("invalid index given!")
                continue

            new_phone = input("new phone: ")
            edit(contacts, index, new_phone)
            print("contact edited.")
            save(contacts, DATA_FILE)

        elif choice == 4:
            for i, c in enumerate(contacts, 1):
                print(f"{i}. {c['name']}: {c['phone']}")
            index = int(input("index: ")) - 1
            if index < 0 or index >= len(contacts):
                print("invalid index. can't delete contact.")
                continue
            
            delete(contacts, index)
            print("deleted successfully.")
            save(contacts, DATA_FILE)

        elif choice == 5:
            if not contacts:
                print("nothing to search.")
                continue

            keyword = input("search: ")
            result = search(contacts, keyword)
            if not result:
                print("nothing found.")
            else:
                for c in result:
                    print(f"{c['name']}: {c['phone']}")

        elif choice == 6:
            save(contacts, DATA_FILE)
            print(f"Saved {len(contacts)} contacts.")

        elif choice == 7:
            print("see you")
            break

        else:
            print("please enter (1-7)")
            continue

if __name__ == "__main__":
    main()