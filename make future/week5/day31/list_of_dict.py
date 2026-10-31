contacts = [
    {"name": "Prem", "phone": "9800000"},
    {"name": "Ram", "phone": "984544324"},
    {"name": "hari", "phone": "98543676"},
]
with open('contacts.txt', 'w', encoding = 'utf-8') as f:
    for contact in contacts:
        for k, v in contact.items():
            f.write(f"{k} | {v}\n")

loaded = []
with open('contacts.txt', 'r', encoding = 'utf-8') as f:
    lines =[line.strip() for line in f if line.strip()]

for i in range(0, len(lines), 2):
    d = {}
    for l in lines[i: i+2]:
        k, v = l.split('|', 1)
        print(k, v)
        d[k.strip()] = v.strip()
        
    loaded.append(d )
 
print(loaded)