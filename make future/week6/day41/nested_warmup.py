import json
from datetime import datetime

collection = {
    "version": 1,
    "contacts":[
        {"name":"jeff", "phone":"123"},
        {"name":"elone", "phone":"456"},
    ],
}

with open('practice.json','w', encoding='utf-8') as f:
    json.dump(collection, f, indent=2, ensure_ascii=False)

with open('practice.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# print(data.get("contacts", []))
for c in data["contacts"]:
    print(f"{c["name"]}: {c["phone"]}")

