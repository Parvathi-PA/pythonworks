
num=int(input("enter the number:"))

reverse=0

while(num!=0):#123!=0
    
  digit=num%10 #123%10=3
  
  reverse=(reverse*10)+digit #0+3=3
  
  num=num//10 #12.3=12
  
print(reverse)#print 3
  
