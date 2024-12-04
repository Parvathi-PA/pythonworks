input=input("enter:").lower()

f=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\word_files.txt")

lst=[]

for word in f:
    
    word=word.rstrip("\n")
    
    words=word.split(" ")
    
    lst.extend(words)
    
    count=lst.count(input)
        
print(count)
    