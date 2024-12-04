#3alphabet
#4th place alphabet[PCAFTH]
#1alpahbet
#4digits
#1aphabet

from re import fullmatch

pancard_num=input("entr num:")

pattern="[A-Z]{3}[PCAFTH][A-Z]{1}[0-9]{4}[A-Z]{1}"

matcher=fullmatch(pattern,pancard_num)

if matcher==None:
    
    print("invalid")
    
else:
    print("valid")