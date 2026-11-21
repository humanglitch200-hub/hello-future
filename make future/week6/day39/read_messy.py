import csv
FIELDS = ['name', 'phone']

def clean_row(row, fields):
    clean = {}
    for field in fields:
        value = row.get(field, "")
        if value is None:
            value = ""
        clean[field] = str(value).strip()
    return clean

def is_valid_row(row, required_fields):
    for field in required_fields:
        if field not in row or row[field] is None:
            return (False, f"missing field: {field}")
    for field in required_fields:
        if not row[field].strip():
            return (False, f"empty field: {field}")
    if None in row:
        return (False, f"extra columns")
    return (True, None)

#writing messy.csv by hand
with open('messy.csv', 'w', newline='', encoding='utf-8') as f:
    f.write("name,phone\n")
    f.write("Alice,123\n")
    f.write("Bob ,456\n")
    f.write("Cara,\n")
    f.write("Dan,789,extra\n")

results = []
with open('messy.csv', 'r', newline = '', encoding='utf-8') as f:
    reader = csv.DictReader(f, skipinitialspace =True)
    for row in reader:
        ok, reason = is_valid_row(row, FIELDS)
        if ok: 
            results.append(clean_row(row, FIELDS))
        else:
            print(f"skipped {row['name']!r}: {reason}")
        clean_row(row, FIELDS)

print(results)
print()

normal_lists = []
#exercise two wrong.csv:
with open('wrong.csv', 'r', newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f, skipinitialspace= True)
    
    #MUST REMEMBER 5: check fieldnames
    if reader.fieldnames != FIELDS:
        print(f"Warning: header is {reader.fieldnames}, excepted {FIELDS}")

        #FIX: normalize to lowercase so row keys match Fields
        reader.fieldnames = [name.strip().lower() for name in reader.fieldnames]

    for row in reader:
        ok, reason = is_valid_row(row, FIELDS)
        if ok:
            normal_lists.append(clean_row(row, FIELDS))
        else:
            print(f"Skipped {row['name']!r}: {reason}")

print(normal_lists)


        