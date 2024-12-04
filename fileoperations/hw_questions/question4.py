# 4. Line Count in a File:
#    - Write a Python program that reads a file and prints the total number of lines in the file.
# 

f=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\text.txt","r")

count=0

for line in f:
    
    count=count+1
print("total number of lines : ",count)
   
f.close()
    
    