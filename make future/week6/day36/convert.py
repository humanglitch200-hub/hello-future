import csv
mew=[]
with open('week5/day31/phonebook.txt','r',encoding='utf-8')as f:
    for l in f:
        l = l.strip()
        if not l:
            continue
        part = l.split("|")
        mew.append(part)

with open('phonebook.csv', 'w', newline='', encoding='utf-8' )as f:
    writer = csv.writer(f)
    writer.writerows(mew)