import csv
try:
    with open('mew.csv','r',newline='', encoding='utf-8')as f:
        f.readlines()

except FileNotFoundError:
    print("File doesnot exists.")

    