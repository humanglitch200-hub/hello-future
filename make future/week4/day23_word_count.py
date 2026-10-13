#Taking input:
sentence = input("Enter a sentence: ")
if sentence =='':
    print("Space is not allowed! enter a sentence.")

words = sentence.lower().split()

#counting 
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

#printing each words
for word, count in counts.items():
    print(f"{word} : {count}")

#printing total unique words:
print("Total unique words: ",len(counts))

#Most common word and its count:
cword = None
cword_count = 0
for word, count in counts.items():
    if not count >= 1:
       if count > cword_count:
          cword_count = count
          cword = word
          print(f"Most common word is: {cword}\nwith {cword_count} occurences.")


    else:
        print("No common word.") 
        break



