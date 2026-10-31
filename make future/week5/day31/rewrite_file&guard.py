
#Load
contacts = []
with open('contacts.txt') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split("|")
# if len(parts) != 2: it is a protector(guard)
        if len(parts) != 2:
            continue
        contacts.append({"name" : parts[0], "phone": parts[1]})

#Change Prem's phone
for c in contacts:
    if c["name"] == "Prem":
        c["phone"] = "99999999999"

#Write back
with open ('contacts.txt', 'w') as f:
    for c in contacts:
        f.write(f"{c['name']} | {c['phone']}\n")

#Load again and print
with open("contacts.txt") as f:
    for line in f:
        print(line.strip())


        ##HELPed by AI I even not able to think now!