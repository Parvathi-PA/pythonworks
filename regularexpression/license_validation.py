

from re import fullmatch

input=input("enter the license num:")

pattern="(DL)(-)[0-9]{13}"

matcher=fullmatch(pattern,input)

if matcher==None:
    
    print("invalid")
    
else:
    print("valid")