import csv
with open('phonebook_h.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["phone"] is None or row["phone"] is None or row["phone"] =='' or row["name"] =='' :
            print(f"Bad row: {row}")
            continue
        print(f"Name: {row["name"]} | Phone: {row["phone"]}")

