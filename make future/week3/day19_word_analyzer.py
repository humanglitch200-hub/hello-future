def analyze(sentence):
    split_sentence = sentence.split()

    unique_only = []          #to see unique word
    longer_words = []         #to see most longer word
    frequencies = {}          #to see how many time a word apprears
    longest = ''              #to find longest word
    for w in split_sentence:
        if w not in unique_only:
            unique_only.append(w)

    for w in split_sentence:
        if len(w) > 4:
            longer_words.append(w)

    for w in longer_words:
        if len(w) > len(longest):
           longest = w

    for w in split_sentence:
        if w in frequencies:
            frequencies[w] += 1
        else:
            frequencies[w] = 1

    # for w in frequencies:    REMEMBER IT, NEEDED WHILE PRINTING!
    #     print(frequencies[w], w)
 
    upper_split_sentence =  []
    for w in split_sentence:
        upper_split_sentence.append(w.upper())

    return { "unique":         unique_only,
            "Longest words":   longer_words,
             "longest":        longest,
             "Frequencies":    frequencies,
             "All upper case": upper_split_sentence
             }

result = analyze("my name is prem , prem is my name is prem treilionare.")
print(result["longest"])

for w in result["Frequencies"]:
    print(result["Frequencies"][w], w)
