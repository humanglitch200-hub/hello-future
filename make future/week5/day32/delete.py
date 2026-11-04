with open('contacts copy.txt', 'r', encoding ='utf-8') as f:
    contacts = f.readlines()
    for i, l in enumerate(contacts):
        print(f'{i+1}. {l.strip()}')
        
    try:
        choice = int(input("delete number(index): "))
        if choice > len(contacts) or choice <= 0:
            print('index out of range')
            raise SystemExit
        
    except ValueError:
        print("ENTER index...")
        raise SystemExit
    
    index = choice -1
    del contacts[index]

with open('contacts copy.txt', 'w', encoding ='utf-8') as f:
    f.writelines(contacts)

with open('contacts copy.txt', 'r', encoding ='utf-8') as f:
    print(f.read())

