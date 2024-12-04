
num=int(input("enter the number:"))#2

is_prime=True

for i in range(2,num+1): #2,2
    
    if num%i==0:#2%2==0  true
        
        is_prime=False
        
        break
    
print(is_prime)