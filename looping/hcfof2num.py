
#hcf of 2 numbrs(gcd)

num1=int(input("enter the number:")) #12


num2=int(input("enter the number:"))#24n

hcf=1

#sequence=range(1,min(num1,num2)+1)
min_number=num1 if num1>num2 else num2

for i in range(1,min_number+1):  #1,2,4,6,8
    
       if num1%i==0 and num2%i==0:#12%1==0 and 24%1==0
        
        
        hcf=i
        
print(hcf)




#lcm


    