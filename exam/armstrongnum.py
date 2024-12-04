
num=int(input("enter the number:")) #234

digit_count=len(str(num))#234 convert to string then only we can take count

total=0 

original=num

while(num!=0):#153!=0
    
    digit=num%10 #153%10=3
    
    exponent=digit**digit_count #3**3=27
    
    total=total+exponent #0+27=27
    
    num=num//10 #153//10=15
    
print("armstorm number" if total==original else "not armstrong")