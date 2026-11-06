import os
print(os.path.exists("week5/day33/contacts.txt"))

with open('test.txt','w', encoding ='utf-8') as f:
    pass

# os.chdir("week5/day33")
print(os.path.exists("test.txt"))

os.remove("test.txt")
print(os.path.exists("test.txt"))

with open('data.txt', 'w', encoding ='utf-8') as f:
    f.write("1\n2\n3")

def backup_files(filename):
    if not os.path.exists(filename):
        return
    with open(filename, 'r', encoding ='utf-8')as f:
        content = f.read()
    with open(filename +'.bak', 'w', encoding='utf-8') as f:
        f.write(content)

backup_files('data.txt')
os.remove('data.txt')
print(os.path.exists("data.txt.bak"))