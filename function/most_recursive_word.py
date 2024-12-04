
text="this is a simple this programming question to find words with maximum number of characters"

words=text.split(" ")

# def get_count(w):
    
#     return words.count(w)

# print(max(words,key=get_count))

#or

# print(max(words,key=lambda w:words.count(w)))



#most recursive character

#non recursive character

text="ABAABBCA"
def get_count(ch):
    return text.count(ch)
print(max(text,key=get_count))

#or

# print(max(text,key=lambda ch:text.count(ch)))

# print(min(text,key=lambda ch:text.count(ch)))