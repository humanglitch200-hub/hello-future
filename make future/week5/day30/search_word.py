word = input("Enter a word: ")
with open('lines.txt', 'r', encoding = 'utf-8')as f:
    for i, l in enumerate(f, start=1):
        if word in l:
            print("Line number is:",i)
            print(l)