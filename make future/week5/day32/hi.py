contacts = [
    {"name": "prem", "phone": 123},
    {"name": "ram", "phone": 623},
]

for i, c in enumerate(contacts, 1):

    print(f"{i}. {c['name']}- {c['phone']}")