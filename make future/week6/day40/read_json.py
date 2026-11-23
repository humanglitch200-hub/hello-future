import json
with open('converted.json', 'r', encoding='utf-8') as f:
    reader = json.load(f)
for c in reader:
        print(f"Name: {c['name']} | Phone: {c['phone']} | Phone type: {type(c['phone']).__name__}")

