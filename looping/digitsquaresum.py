
number=int(input("enter the number:"))

sum=0

while(number!=0):#5!=0
    
    digit=number%10 #25%10=5
    
    square=digit**2 #5*5=25
    
    sum=sum+square #0+5=5
    
    number=number//10 #25//10=2
    
print(sum)