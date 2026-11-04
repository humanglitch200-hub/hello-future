#THis was only my try -- The code doesn't work...

with open('contacts.txt', 'r', encoding='utf-8') as f:
    for i, l in enumerate(f):
        print(f.write(f'{i+1}. {l.split()}\n '))

with open('contacts.txt', 'r', encoding='utf-8') as f:
        for l in f:
            if not l:
                 print("Nothing to delete")
            else:     
                try:
                    choice = int(input("Enter index of line to delete: "))
                except ValueError:
                    print("Enter valid index.")
                if choice in l:
                    del l
                f.write(f'{l.split()}\n')

with open('contacts.txt', 'r', encoding ='utf-8') as f:
    print(f.read().split())