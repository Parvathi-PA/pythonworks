# Read Even Lines from a File:
#    - Create a Python program that reads and prints only the even-numbered lines from a file.


# f_read=open("C:\\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\word_files.txt")

# for i,line in enumerate(f_read,start=1):
    
#     if i%2==0:
    
#      print(line)
    
# f_read.close()


# Find Duplicate Lines in a File:
# - Create a program to check for and print duplicate lines in a file.


# f=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\word_files.txt")

# duplicate_line={}

# for line in f:
#     line=line.rstrip("\n")
    
#     if line in duplicate_line:
        
#         duplicate_line[line]+=1
#     else:
#         duplicate_line[line]=1

# line_count={k for k,v in duplicate_line.items() if v>1}


# print(line_count) 





# 12. Character Frequency in a File:
# - Write a Python program that counts the frequency of each character in a text file.
# 
# 

# f=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\word_files.txt")

# character=[]

# for line in f:
    
#     line=line.rstrip("\n")
    
#     for ch in line:
        
#         character.extend(ch)
        
# char_count={ch:character.count(ch) for ch in character}

# print(char_count)
        
        
        
# 13. Remove Blank Lines from a File:
    # - Write a program that removes all blank lines from a given text file.
    
# f=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\text.txt")


# for line in f:
     
#      line=line.rstrip("\n")
     
# f.close()
     
# f_write=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\text.txt","w")

     
# f_write.write(line)
     

# f_write.close()








# 14. Search and Replace Text:
    # - Write a program that searches for a specific word in a file and replaces it with another word.
# 

f_read=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\students.txt")

read=f_read.read()
    
f_read.close()

new_word=read.replace("wilson","hallo my name is ")

f_write=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\students_name.txt","w")

for line in read:
    
    f_write.write(new_word)
    
f_write.close()
    
    