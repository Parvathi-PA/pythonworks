
from re import fullmatch

user_input=input("enter input:")

pattern="[a-zA-z][a-zA-Z0-9]*"

matcher=fullmatch(pattern,user_input) #none

if matcher==None:
    
    print("invalid")
    
else:
    print("valid")