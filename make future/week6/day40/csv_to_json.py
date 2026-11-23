import json, csv
FIELDS = ['name', 'phone']

def is_valid_row(row, required_fields):
    for field in required_fields:
        if field not in row or not isinstance(row[field], str) or not row[field].strip():
            return (False, f'Bad or Misiing field: {field}')
    return (True, None)

def clean_row(row, fields):
    clean = {}
    for field in fields:
        value = row.get(field, "")
        if value is None:
            value = ""
        clean[field] = str(value).strip()
    return clean

DATA_FILE = DATA_FILE = '/home/prem/python/hello-future/make future/week6/day39/phonebook_v9_hardened.csv'   
with open(DATA_FILE, 'r', encoding='utf-8') as f:
    result = []
    reader = csv.DictReader(f, skipinitialspace=True)
    for row in reader:
        ok, reason = is_valid_row(row, FIELDS)
        if ok:
            result.append(clean_row(row, FIELDS))
        else:
            print(f"the row is skipped becuase of: {reason}")

with open('converted.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

with open('converted.json') as f:
    data = json.load(f)
print(type(data))
for c in data:
    print(type(c), type(c['name']), type(c['phone']))
            
