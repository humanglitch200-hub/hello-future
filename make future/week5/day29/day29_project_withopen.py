def add_notes(note):
    if not note:
        return None
    with open('note.txt', 'a', encoding = 'utf-8')as f:
        f.write(note +'\n')

def view_notes():
    try:
        with open('note.txt', 'r', encoding = 'utf-8') as f:
            for line in f:
                print(line, end = '')

    except FileNotFoundError:
        print('No such file found')

def delete_all():
    try: 
        with open('note.txt', 'w', encoding = 'utf-8') as f:
            f.write('')
    except FileNotFoundError:
        print("No such file exict...") 

if __name__ == "__main__":
    while True:
        print()
        print('1. Add Notes')
        print('2. See all Notes')  
        print('3. Delete all Notes') 
        print('3. Quit')   
        try:
            choice = int(input("Your choice: "))
        except ValueError:
            print("Enter valid choice.")
            continue
        if choice == 1:
            notes = input("Enter Note: ")
            note = notes.lower().strip()
            add_notes(note)
            print('Note has been recorded....')
     
        elif choice == 2:
            print('--- Showin Notes---')
            view_notes()

        elif choice == 3:
            delete_all()
            print("All files have been DElETED...")
            
        elif choice == 4:
            print("See You!")
            break

        else:
            print("Enter (1-2): ")
            continue
            





    
    