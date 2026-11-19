import csv
with open('exercise.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['name','phone']
    writer = csv.DictWriter(f, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerow({"name": "prem", "phone":123})
    writer.writerow({"name": "jef, f", "phone":345})
    writer.writerow({"name": "'ram'", "phone":678})
    writer.writerow({"name": "mew", "phone":"line1\nline2"})

with open('exercise.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"Name: {row['name']}  Phone: {row['phone']}")