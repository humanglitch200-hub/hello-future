import csv
with open('hi.csv', 'w', newline='', encoding='utf-8')as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(["hello, world"])

with open('hi.csv', 'r', newline='', encoding='utf-8')as f:
    print(f.read()) 