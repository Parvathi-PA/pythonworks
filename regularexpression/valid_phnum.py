

#rule 10 digit
#validate mobile num

#+ atleat one
#? optional


from re import fullmatch

user_input=input("enter number:")

pattern="(91)?\d{10}"

matcher=fullmatch(pattern,user_input)

if matcher==None:
    print("invalid")
    
else:
    print("valid")