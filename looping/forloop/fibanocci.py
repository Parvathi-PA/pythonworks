

prev=0

current=1

print(prev)

print(current)

for i in range(1,8):
    
    next=prev+current
    
    print(next)
    
    prev=current
    
    current=next
    
  
  #number=51
  #check 51 is present in fibanocci series?
  
  
number=int(input("enter the number:"))
    
prev=0
  
curent=1

is_fibanocci=False

for i in range(1,number+1):
       
    next=prev+current  
    
    prev=current
    
    current=next
    
    if next==number:
    
     is_fibanocci=True
     
     break
     
print(is_fibanocci)