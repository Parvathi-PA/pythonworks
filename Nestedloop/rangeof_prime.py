

#print prime numbers from start to end


start=int(input("enter the start:")) #5

end=int(input("enter the limit:"))#10

for num in range(start,end+1): #5,6,7,8,9,10
    
    is_prime=True #5 prime true
    
    for i in range(2,num):#2,5
        
        if num%i==0:#6%2
            
            is_prime=False
            
            break
    
    if is_prime==True:
        
        print(num)
    
    
