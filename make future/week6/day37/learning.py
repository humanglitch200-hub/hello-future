import csv

with open('names.csv', 'w', newline='') as f:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Prem', 'last_name': 'Bhandari'})
    writer.writerow({'first_name': 'Mew', 'last_name': 'Hi'})

with open('names.csv', mode='w', newline='') as f:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'jhon', 'last_name': 'kuwar'})

with open('names.csv', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['first_name'], row['last_name'])

with open('names.csv',  'r', newline='') as f:
    csv_reader = csv.DictReader(f)
    line_count = 0
    for r in f:
        if line_count == 0:
            print(f'Column names are {', '.join(row)}')
            line_count += 1
        print(f'\t{row['first_name'], row['last_name']}')
        line_count += 1
    print(f'Processed {line_count} lines.')