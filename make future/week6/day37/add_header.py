import csv
contacts = []
with open('phonebook.csv','r', newline='', encoding='utf-8')as f:
    reader = csv.reader(f)
    for r in reader:
        contacts.append(r)
print(contacts)

with open('phonebook_h.csv', 'w', newline='', encoding='utf-8')as f:
    fieldnames = ['names', 'phone']
    writer = csv.DictWriter(f, fieldnames = fieldnames)
    writer.writeheader()
    for r in contacts:
        if len(r) < 2:
            print(f"Skipping bad row {r}")
            continue
        writer.writerow(dict(zip(fieldnames, r)))


