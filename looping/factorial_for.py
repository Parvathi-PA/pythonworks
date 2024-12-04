

#print factorial of a number

number=int(input("enetr the number:"))

fact=1

for num in range(1,number+1):
    
    fact=num*fact
    
print(fact)