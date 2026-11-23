contacts = [{"name": "Alice", "phone": "123"},
            {"name": "Prem", "phone": 567},
            {"name": "राम", "phone": "1232"}]
import json
with open('cat warmup.json', 'w', encoding='utf-8') as f:
    json.dump(contacts, f, indent=2, ensure_ascii=False)


for c in contacts:
    print(c)

try:
    with open("cat warmup.json", "r", encoding="utf-8") as f:
        data =  json.load(f)
    print("Loaded:", data)

except json.JSONDecodeError as e:
    print(f"Bad json: {e}")

print("Script is still running")

