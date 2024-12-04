
stu_name=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\students_name.txt")
fail_stu=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\failed_stu.txt")

all_stu_pass=set()

failed_stu=set()

for name in stu_name:
    
    all_stu_pass.add(name.rstrip("\n"))
    
for student in fail_stu:
    
    failed_stu.add(student.rstrip("\n"))

passed_students=all_stu_pass.difference(failed_stu)

print(passed_students)