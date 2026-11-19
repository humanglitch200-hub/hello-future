import csv
with open('warmup.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow([''])
    writer.writerow(['smith, john'])
    writer.writerow(['he said "hi"'])

with open('warmup.csv', 'r', newline='', encoding='utf-8')as f:
    reader= csv.DictReader(f)
    for r in reader:
        print(r)

with open('warmup2.csv', 'w', newline='', encoding='utf-8' )as f:
    writer = csv.writer(f, delimiter=',', quoting= csv.QUOTE_ALL)
    writer.writerow([''])
    writer.writerow(['smith, john'])
    writer.writerow(['He said "hi"'])

with open('warmup2.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for l in reader:
        print(l)


with open('warmup2.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'phone'])
    writer.writeheader()                         
    writer.writerow({'name': 'elone', 'phone': 'line1\nline2'})

with open('warmup2.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

print(f"Number of rows: {len(rows)}")
print(repr(rows[0]['phone']))
