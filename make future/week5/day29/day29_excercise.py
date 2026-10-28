with open('day29_note.txt', 'w',encoding = 'utf-8')as f:
    f.write("Hi this is my first open file program...")
with open('day29_note.txt', 'r', encoding = 'utf-8') as f:
    print(f.read())

with open('day29_note.txt', 'w', encoding ='utf-8') as f:
    f.write("Everything is gone!")
with open('day29_note.txt', 'r', encoding = 'utf-8') as f:
    print(f.read())
#Everything is gone!

# with open('hi.txt', 'r', encoding = 'utf') as f:
#         print(f.read())
#FileNotFoundError: No such file found 'hi.txt' -- it is case on it.

#let's try it with try except:
try:
    with open('hi.txt', 'r', encoding = 'utf') as f:
        print(f.read())

except FileNotFoundError:
    print("No such file exicts.")


with open('day29_note.txt', 'a', encoding = 'utf-8') as f:
    f.write("\nHi, I think old data is not gone!")


with open('day29_note.txt', 'r', encoding = 'utf-8') as f:
    print()
    print(f.read())