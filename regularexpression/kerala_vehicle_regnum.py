

#start with KL
#2digit
#alphabet min1 nad max2
#4digit

from re import fullmatch

input=input("enter number:")

pattern="(KL|kl)[0-9]{2}[A-Z]{1,2}[0-9]{4}"

matcher=fullmatch(pattern,input)

if matcher==None:
    
    print("invalid")
    
else:
    print("valid")
    
#passport
#aadhar num
#driving licence