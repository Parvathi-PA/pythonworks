

# num

# 1,num

# write a pgm to check number is perfect or not

num=int(input("entr the number:"))


total=0

for i in range(1,num):
    
   if  num%i==0:
       
       total=total+i
       
print("perfect" if total==num else "not perfect")
































