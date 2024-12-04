
#2. Append and Display File Content:
#    - Create a program that appends user input to an existing file and then displays the entire content of the file.

user_input=input("enter details:")

f=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\students.txt","a")

f.write(user_input +"\n")

f.close()
