# 3. given a string

# text = "this is a simple python program that print most recursive word . this program is simple" 

# write a program to print most frequent word


text = "this is a simple python program that print most recursive word . this program is simple" 

words=text.split(" ")

def word_count(w):
    
    return words.count(w)

print(max(words,key=word_count))
    
    