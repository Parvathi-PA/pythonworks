
f=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\frame_works.txt","a",)

frameworks=["wordpress","springboot","odo","fastapi"]

for fw in frameworks:
    
    f.write(fw + "\n")
    
f.close()