#5. Copy File Content:
#    - Create a program to copy content from one file to another.

# read_file=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\names.txt")

# write_file=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\sentance.txt","w")

# for name  in read_file:
    
#     write_file.write(name + "\n")
    
# read_file.close()
# write_file.close()











# 6. Find Longest Word in a File:
#    - Write a program that finds and prints the longest word in a text file.

f=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\names.txt")


for line in f:
    
    all_words=line.split(" ")     

    for w in all_words:
        
        
        lambda w: len(w)

print(max(all_words,key=lambda w: len(w)))
 
