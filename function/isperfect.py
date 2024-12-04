

def is_perfect_num(number):
    
    original_num=number
    
    total=0
    
    for i in range(1,number): #1,2,3,4,5,6
        
       if number%i==0:#6%1==0
       
        total=total+i
       
    return "perfect" if  total==original_num else "not perfect"   
             
print(is_perfect_num(28))