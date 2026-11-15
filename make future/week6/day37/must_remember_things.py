import csv
contacts = [
    {'name': 'Alice', 'phone':'123'},
    {'name':  'Bob', 'phone': '456'},
]

with open('contacts.csv', 'w', newline='', encoding='utf-8')as f:
    fieldnames = ['name', 'phone']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(contacts)

with open('contacts.csv', 'r', newline='', encoding='utf-8')as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)

with open("contacts.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)