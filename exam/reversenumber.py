

number=int(input("enter the  number:"))

reverse=0

while (number!=0):
    
    digit=number%10 #123%10=3
    
    reverse=reverse*10+digit #0+3=3
    
    number=number//10
    
print(reverse)
    