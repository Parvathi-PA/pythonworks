
#digit  sum

number=int(input("enter the number:"))

total=0

while(number!=0): #234!=0
    
    digit=number%10 #234%10=4
    
    total=digit+total #0+4=4
    
    number=number//10 #234//10=23
    
print(total)

