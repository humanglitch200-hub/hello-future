import csv, os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, '..', 'day37', 'phonebook_h.csv')

def is_valid_row(row, required_field):
    for field in required_field:
        if field not in row or row[field] is None:
            return(False, f"missing field: {field}")
    for field in required_field:
        if not row[field].strip():
            return (False, f"empty field: {field}")
    if None in row:
        return (False, "extra columns")
    return (True, None)

with open(DATA_FILE, 'r', newline='', encoding='utf-8') as f:
    reader= csv.DictReader(f)
    for row in reader:
        ok, reason = is_valid_row(row, ["name", "phone"])
        if ok:
            print(f"Ok: Name: {row['name']} | Phone: {row['phone']}")
        else:
            print(f"{reason}: {row}")