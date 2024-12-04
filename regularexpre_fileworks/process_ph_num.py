
from re import fullmatch

f=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\regularexpre_fileworks\\phone_num.txt")

for num in f:
    
    phone=num.rstrip("\n")
    
    pattern="(91)?[0-9]{10}"
    
    matcher=fullmatch(pattern,phone)
    
    if matcher!=None:
        
        print(phone)