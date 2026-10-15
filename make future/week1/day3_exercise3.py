name = input ("What's your name? ")
print(name.upper())
print(name.title())
print(len(name.replace(" ", "")))

for word in name.split():
    print(word[0])