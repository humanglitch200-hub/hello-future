import os
def load_contacts(filename):
    if not os.path.exists(filename):
        if os.path.exists(filename + '.bak'):
            restore_from_backup(filename)
            print("Recovered from backup.")
    if os.path.exists(filename):
        with open(filename, 'r', encoding = 'utf-8') as f:
            return f.readlines()
    return []

def backup_file(filename):
    if not os.path.exists(filename):
        return
    with open(filename, 'r', encoding ='utf-8')as f:
        content = f.read()
    with open(filename +'.bak', 'w', encoding='utf-8') as f:
        f.write(content)

def save_contacts(filename, contacts):
    backup_file(filename)
    with open(filename, 'w', encoding = 'utf-8') as f:
        for c in contacts:
            f.write(c.rstrip('\n') + '\n')

def restore_from_backup(filename):
    if not os.path.exists(filename + '.bak'):
        print("backup not available")
        return False
    with open(filename +'.bak', 'r', encoding = 'utf-8') as f:
        backup= f.read()
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(backup+'\n')
    return True

print(load_contacts("week5/day33/contacts.txt"))
# contacts = load_contacts("week5/day33/contacts.txt")
# contacts.append("mew | 989\n")
# save_contacts("week5/day33/contacts.txt", contacts)

# #Verify
# os.chdir("week5/day33")
# print(os.listdir("."))

# print("--old--")
# print(open("contacts.txt.bak").read())

# print("--new--")
# print(open("contacts.txt").read())

# restore_from_backup("week5/day33/contacts.txt")


