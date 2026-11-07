import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PHONEBOOK_FILE = os.path.join(BASE_DIR, "phonebook.txt")
BACKUP_FILE = os.path.join(BASE_DIR, "phonebook.txt.bak")

def backup_file(filename):
    if not os.path.exists(filename):
        return
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    with open(filename + '.bak', 'w', encoding='utf-8') as f:
        f.write(content)

def restore_from_backup(filename):
    if not os.path.exists(filename + '.bak'):
        print("backup not available")
        return False
    with open(filename + '.bak', 'r', encoding='utf-8') as f:
        content = f.read()
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    return True

def load(contacts, filename):
    contacts.clear()
    if not os.path.exists(filename):
        if os.path.exists(filename + '.bak'):
            restore_from_backup(filename)
            print("Recovered from backup")
        else:
            return contacts
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                if len(parts) != 2:
                    continue
                contacts.append({"name": parts[0], "phone": parts[1]})
    return contacts

def save(contacts, filename):
    backup_file(filename)
    with open(filename, 'w', encoding='utf-8') as f:
        for c in contacts:
            f.write(f"{c['name']}|{c['phone']}\n")

def add(contacts, name, phone):
    contacts.append({"name": name, "phone": phone})

def search(contacts, find):
    result = []
    for c in contacts:
        if find.lower() in c['name'].lower() or find in c['phone']:
            result.append(c)
    return result

def edit(contacts, index, new_phone):
    contacts[index]['phone'] = new_phone

def delete(contacts, index):
    del contacts[index]

def main():
    contacts = []
    contacts = load(contacts, PHONEBOOK_FILE)
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
        print("6. Surprise")
        print("7. File info")
        print("8. Quit")

        try:
            choice = int(input("choice: "))
        except ValueError:
            print("invalid choice.")
            continue

        if choice == 1:
            name = input("name: ")
            phone = input("phone: ")
            add(contacts, name, phone)
            save(contacts, PHONEBOOK_FILE)

        elif choice == 2:
            for c in contacts:
                print(f"{c['name']}: {c['phone']}")

        elif choice == 3:
            find = input("search: ")
            result = search(contacts, find)
            if result:
                for c in result:
                    print(f"{c['name']}: {c['phone']}")
            else:
                print("no match")

        elif choice == 4:
            if not contacts:
                print("nothing on file")
                continue
            for i, c in enumerate(contacts, 1):
                print(f"{i}. {c['name']}: {c['phone']}")
            try:
                i = int(input("index: "))
                index = i - 1
                if index >= len(contacts) or index < 0:
                    print("invalid index")
                    continue
            except ValueError:
                print("invalid index")
                continue
            new_phone = input("new number: ")
            edit(contacts, index, new_phone)
            print("number edited.")
            save(contacts, PHONEBOOK_FILE)

        elif choice == 5:
            if not contacts:
                print("nothing to delete")
                continue
            for i, c in enumerate(contacts, 1):
                print(f"{i}. {c['name']}: {c['phone']}")
            try:
                i = int(input("index: "))
                index = i - 1
                if index >= len(contacts) or index < 0:
                    print("invalid index")
                    continue
            except ValueError:
                print("invalid input!")
                continue
            delete(contacts, index)
            print("contact removed.")
            save(contacts, PHONEBOOK_FILE)

        elif choice == 6:
            mew = "phonebookV5_anypath.py"
            print(os.path.getsize(mew))
            print(os.path.basename(mew))
            with open(mew, 'r') as f:
                lines = 0
                for l in f:
                    lines += 1
            print(lines)

        elif choice == 7:
            print(f'full path: {PHONEBOOK_FILE}')
            if os.path.exists(PHONEBOOK_FILE):
                print(f'size in bytes: {os.path.getsize(PHONEBOOK_FILE)}')
            print(f"Backup file: {BACKUP_FILE}")
            print(f"file exists: {os.path.exists(BACKUP_FILE)}")
    
        elif choice == 8:
            print("see you.")
            break

        else:
            print("enter valid choice")


if __name__ == "__main__":
    main()   
                    