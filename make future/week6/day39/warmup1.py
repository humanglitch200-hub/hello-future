import csv

# Write by hand: space after the comma
with open('warmup1', 'w', newline='', encoding='utf-8') as f:
    f.write("name,phone\n")
    f.write("Clice, 123\n")

#Read WITHOUT skipinitialspace=True
with open('warmup1', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for c in reader:
        print(F"NO SKIP: {c['name']}: {c['phone']}")

#Read WITH skipinitialspace=True
with open('warmup1', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f, skipinitialspace=True)
    for c in reader:
        print(f"with skip: {c['name']}: {c['phone']}")

with open('warmup1', 'w', newline='', encoding='utf-8') as f:
    f.write("mew; 123\n")

with open('warmup1', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=';', skipinitialspace=True)
    for n in reader:
        print(n)

