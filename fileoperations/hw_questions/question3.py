
# 3. Word Count in a File:  - Write a program to count the number of words in a given text file.

f=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\text.txt","r")

all_words=[]

word_count=[]

for line in f:
    
    line=line.rstrip("\n")
    
    all_words.extend(line.split(" "))
            
word_count={w:all_words.count(w) for w in all_words}
        
print(word_count)

