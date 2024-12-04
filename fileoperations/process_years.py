
year_path="C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\years.txt"

centuary="C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\centuary_year.txt"

leap="C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\leap_year.txt"

f_year=open(year_path,"r")

f_century=open(centuary,"w")

f_leap=open(leap,"w")

def century_year(year):
    
    return True if year%100==0 else False

def leap_year(year):
    
    if year%100==0 and year %400==0 or year%100!=0 and year%4==0:
        
        return True
    else:
        
        return False
    
for year in f_year:
    
    year=int(year)
    
    if century_year(year):
    
     f_century.write(str(year) + "\n")
     
    if leap_year(year):
        
        
        f_leap.write(str(year) + "\n")
        
f_year.close()

f_century.close()

f_leap.close()