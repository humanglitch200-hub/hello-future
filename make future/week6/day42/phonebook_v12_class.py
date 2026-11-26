import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "phonebook_v12.json")
FIELDS = ["name", "phone"]

def is_valid_row(row, required_fields):
    for field in required_fields:
        if field not in row or row[field] is None:
            return (False, f"missing or bad field: {field}")

    for field in required_fields:
        if not row[field].strip():
            return (False, f"empty field: {field}")
        
    if None in row:
        return(False, "extra columns")
    return (True, None)

def clean_row(row, fields):
    clean = {}
    for field in fields: 
        value = row.get(field, "")
        if value is None:
            value = ""
        clean[field] = str(value).strip()
    return clean

class Phonebook:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = []
        self.load()

    def load(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, list):
                    self.contacts = data
                else: 
                    self.contacts = data.get("contacts", [])
        except FileNotFoundError:
            self.contacts = []
        except json.JSONDecodeError as e:
            print(f"warning: {e}")
            self.contacts = []

    def save(self):
        payload = {"version": 1, "contacts": self.contacts}
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(payload, f, indent = 2, ensure_ascii=False, sort_keys=True)

    def is_duplicate(self, name):
        for c in self.contacts:
            if c["name"] == name:
                return True
        return False
    
    def add (self, name, phone):
        row ={"name": name, "phone": phone}
        ok, reason = is_valid_row(row, FIELDS)
        if not ok:
            print(f"BAD row: {reason}")
            return False

        duplicate = self.is_duplicate(name)
        if duplicate:
            want = input(f"The name({name}) exists twice.save though(y/n): ")
            if want not in ('y', 'yes'):
                return False
        
        self.contacts.append(clean_row(row, FIELDS)) 
        self.save()
        print("contact added.")
        return True

    def edit(self, index, new_phone):
        new_phone = new_phone.strip()
        if new_phone in ("", " "):
            print("phone cannot be empty.")
            return False
        self.contacts[index]['phone'] = new_phone
        self.save()
        print("contact edited.")
        return True

    def delete(self, index):
        del self.contacts[index]
        self.save()
        print("contact deleted.")
        return True

    def search (self, keyword):
        result = []
        keyword = keyword.lower()
        for c in self.contacts:
            if keyword in c['name'] or keyword in c['phone']:
                result.append(c)
        return result

    def view(self):
        for c in self.contacts:
            print(f"{c['name']}: {c['phone']}")

def main():
    pb = Phonebook(DATA_FILE)

    if pb.contacts:
        print(f"loaded {len(pb.contacts)} contacts.")
    else:
        print("starting fresh.")

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
            print("only numbers(1-7)!")
            continue

        if choice == 1:
            name = input("name: ")
            phone = input("phone: ")
            if phone in ("", " ") or name in ("", " "):
                print("enter valid info.")
                continue

            pb.add(name, phone)

        elif choice == 2:
            for i, c in enumerate(pb.contacts, 1):
                print(f"{i}. {c['name']}: {c['phone']}")
            try:
                index = int(input("index: ")) -1
                if index <0 or index >= len(pb.contacts):
                    print("invalid index!")
                    continue
            except ValueError:
                print("Value Error. Enter number!")
                continue

            new_phone = input("new phone: ")
            pb.edit(index, new_phone)

        elif choice == 3:
            pb.save()

        elif choice == 4:
            for i, c in enumerate(pb.contacts, 1):
                print(f"{i}. {c['name']}: {c['phone']}")

            try:
                index = int(input("index: ")) - 1
                if index < 0 or index >= len(pb.contacts):
                    print("invalid index.")
                    continue

            except ValueError:
                print("Value Error. Enter number!")
                continue

            pb.delete(index)

        elif choice == 5:
            keyword = input("search: ").lower()
            result = pb.search(keyword)
            if not result:
                print("no match")
            else:
                for c in result:
                    print(f"{c['name']}: {c['phone']}")

        elif choice == 6:
            pb.view()

        elif choice == 7:
            print("bye!")
            break

        else:
            print("choice must be between (1-7).")
            continue

if __name__ == "__main__":
    main()