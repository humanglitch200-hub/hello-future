import csv

details = [
    ["prem", "123"],
    ["mew", "567"],
    ["hi", "342"]
]

with open('warmup.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerows(details)   