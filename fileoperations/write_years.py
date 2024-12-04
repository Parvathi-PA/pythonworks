
f=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\years.txt","w")


for year in range(1800,2025):
    
    f.write(str(year) +"\n")
    
f.close()