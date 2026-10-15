ask = input("Write about your self: ")

including_space = len(ask)

excluding_spaces = len(ask.replace(' ', ''))

word_count = len(ask.split())

#Total sentences (count, ?.!)
total_sentences = sum (1 for c in ask if c in ".!?")

#Upper case
uppercase = ask.upper()

#Text Reversed
reversed_text = ask[::-1]

#MOst common character (excluding spaces)
char_count = {}
for c in ask:
    if c != ' ':
        char_count[c] = char_count.get(c, 0) + 1

most_common_char = max(char_count, key= char_count.get)

print(including_space )
print(excluding_spaces)
print(word_count)
print(total_sentences)
print(uppercase)
print(reversed_text)
print(most_common_char )
