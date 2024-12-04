
#lowercase
#start with an alphabet
#numbers optional
#@gmail.com
#before at 6 to 64 character

from re import fullmatch

gmail=input("enter :")

pattern="[a-z]+[0-9a-z]{5,63}@gmail.com"

matcher=fullmatch(pattern,gmail)

if matcher==None:
    
    print("invalid")
    
else:
    print("valid")