import json, os

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "wrapped.json")   

with open(DATA, 'r', encoding='utf-8') as f:
    data = json.load(f)

version = data.get("version", 1)
contacts = data.get("contacts", [])
print(f"Version: {version} "
      f"Contacts: {len(contacts)}")

if not contacts:
    print("nothing to print.")
else:    
    for c in contacts:
        print(f"{c['name']}: {c['phone']}")
        # it is name of file on day41: wrapped.json