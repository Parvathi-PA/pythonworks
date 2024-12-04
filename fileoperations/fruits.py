

s=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\fruits.txt","r")

#we can add this to a list

fruits=[]

for line in s:
    
    fruits.append(line.rstrip("\n"))
    
print(fruits)