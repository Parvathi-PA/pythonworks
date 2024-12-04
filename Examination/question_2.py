

#print maximum number of word

text="this is a simple question return word with maximum number of characters"

words=text.split(" ")

max_len_word=max(words,key=lambda w:len(w))
print(max_len_word)