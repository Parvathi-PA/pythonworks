
from re import fullmatch

pass_num=input("enter the num:")

pattern="[A-Z]{2}[1-9]{1}[0-9]{1}[0-9]{3}[1-9]"

matcher=fullmatch(pattern,pass_num)

if matcher==None:
     
     print("invalid")
     
else:
    print("valid") 