search = str(input("Search name: "))
matches = []
with open('contacts copy.txt', 'r', encoding='utf-8') as f:
    contacts = f.readlines()
    for c in contacts:
        found = False
        if search.lower() in c.lower():
            matches.append(c)
            found = True
        if found:
            print(matches)  

    