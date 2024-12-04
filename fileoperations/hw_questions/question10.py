

f1_read=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\students_name.txt","r")

f2_read=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\students.txt","r")

f_write=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\newstudents.txt","w")

for line in f1_read:
    
    f_write.write(line)
    
for lin in f2_read:
    
    f_write.write(lin)
    
f_write.close()

f1_read.close()

f2_read.close()