

text="this is a simple programming question to find words with maximum number of characters"

# split the sentance

words=text.split(" ")

# def get_length(w):
#     return len(w)

# print(max(words,key=get_length))

# or 

lambda w: len(w)

print(max(words,key=lambda w: len(w)))


