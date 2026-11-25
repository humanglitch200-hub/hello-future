from datetime import datetime
import json

data = {
    "version": 1,
    "contacts": [
        {"name":"Jeff", "phone":"123"},
        {"name":"elone", "phone": "456"},
    ],
}

def handler(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    return str(obj)

with open('contacts.json', 'w', encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

with open('contacts.json', 'r', encoding="utf-8") as f:
    data = json.load(f)
    data = {"saved": datetime.now()}
    json.dump(data, open('contacts.json', 'w'), default=handler)

print(data["version"])
print(data["contacts"][1])



