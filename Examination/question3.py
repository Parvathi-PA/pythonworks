

# text="Hello world! hello everyone".lower()

text=" A string text containing the text to analyze".lower()

words=text.split(" ")

def most_frequesnt_word(w):
     
     return words.count(w)
     most_frequesnt_word=lambda w:words.count(w)
     
print(max(words,key=most_frequesnt_word))

