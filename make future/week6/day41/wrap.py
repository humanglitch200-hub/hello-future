import json, os

BASE_FILE = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_FILE, "..", "day40", "phonebok_v10.json")

with open(DATA_FILE, 'r', encoding = 'utf-8') as f:
    data = json.load(f)

with open('wrapped.json', 'w', encoding='utf-8') as f:
    json.dump({"version":1, "contacts": data}, f, indent=2, ensure_ascii=False, sort_keys=True)

