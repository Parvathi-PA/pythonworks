
#sort the words in the text in ascenting order

text="this is a simple programming question to find words with maximum number of characters"

words=text.split(" ")

# def get_length(w):
    
#     return len(w)

# sort_words=sorted(words,key=get_length,reverse=True)
# print(sort_words)


sort_words=lambda w:len(w) 

print(sorted(words,key=sort_words,reverse=True))

#most recursive

