import csv
comp1 = []
comp2 = []
with open('warmup.csv', 'w', newline='', encoding='utf-8')as f:
    fieldnames= ['name','phone']
    writer = csv.DictWriter(f, fieldnames = fieldnames)

    writer.writeheader()
    writer.writerow({'name': 'prem', 'phone':123})
    writer.writerow({'name': 'hi', 'phone': 456})

with open('warmup.csv','r', newline='', encoding='utf-8')as f:
    reader = csv.DictReader(f)
    print(reader.fieldnames)
    comp1.append(reader)
    for row in reader:
        print(row)

mew_lst = [
    {'name': 'premium', 'phone':923},
    {'name': 'jef', 'phone':546}
]

with open('mew.csv', 'w', newline='', encoding='utf-8') as f:
    fieldnames = ['name','phone']
    writer = csv.DictWriter(f, fieldnames= fieldnames)

    writer.writerows(mew_lst)

with open('mew.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    comp2.append(reader)
    for row in reader:
        print(row)

print(comp1 == comp2)

with open('warmup.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if not row['phone'] :
            print(f'Bad row: {row}')
#It will never arun because rest of code filters that out!