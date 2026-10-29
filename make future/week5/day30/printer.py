with open('lines.txt', 'w', encoding='utf-8') as f:
    f.write('sayo-nara\nnamaste\nhi\nramram')

with open('lines.txt', 'r', encoding ='utf-8') as f:
    for line in f:
        print(line, end ='')

