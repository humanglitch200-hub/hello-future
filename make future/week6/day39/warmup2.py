def clean_row(row, fields):
    clean = {}
    for field in fields:
        value = row.get(field,"")
        if value is None:
            value =""
        clean[field]= str(value).strip()
    return clean

mew = clean_row({"name": " Alice ", "phone": None, "mew": "123"}, ["name", "phone"])
print(mew)

contacts = [
    {"name": "sushmita", "age": "23"},
    {"name": "sushmita", "age": "101"},
]

def is_duplicate(contacts, name):
    for c in contacts:
        if c["name"].lower() ==  name.lower():
            return True
    return False

print(is_duplicate(contacts, "Sushmita"))
print(is_duplicate(contacts, "Alice"))
