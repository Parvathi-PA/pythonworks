# 1. Write and Read a File:
#    - Write a program to take input from the user and write it to a file. Then, read the content from the file and display it.


user_input=input("enter a string:")

f=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\hallo_world.txt","w")

f.write(user_input)

f.close()



read_file=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\hallo_world.txt","r")

for line in read_file:
      
      print(line)
 
read_file.close()