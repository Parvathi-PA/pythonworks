
# start with an alphabet from p-t
#in second place must be a number this is \ by 3
#follwed by any number alphabets and @

from re import fullmatch

user_input=input("enter input:")

pattern="[p-tP-T][369][0-9a-zA-Z@]*"

matcher=fullmatch(pattern,user_input)

if matcher==None:
    print("invalid")
    
else:
    print("valid")

