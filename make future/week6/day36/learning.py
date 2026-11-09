import csv
with open('eggs.csv', newline='') as csvfile:
    spamreader = csv.read(csvfile, delimeter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))

#where eggs.csv cotains: Spam Spam Spam Spam Spam |Baked Beans|
#Spam |Lovely Spam| |Wonderful Spam|

with open('employee_birthday.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimeter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Cloumn names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')


with open('employee_birthday.csv', mode='r') as csv_file:
    csv__reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f"Column names are {", ".join(row)}")
            line_count += 1
        print(f'\t{row["name"]} works in the {row["department"]}'
              f'department, and was born in {row["birthday month"]}.')
        line_count += 1 
    print(f'Processed {line_count} lines.')




#must remember things:
import csv
with open("data.csv", 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Alice", "123"])
    writer.writerows([["Bob", "456"], ["cara", "789"]])

with open("data.csv", "r", newline="", encoding="utf-8")as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
--
