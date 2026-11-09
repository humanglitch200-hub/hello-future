import csv
with open('phonebook.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) < 2:
            print(f"Skipping bad row: {row}")
            continue
        print(f"Name: {row[0]} | Phone: {row[1]}")
