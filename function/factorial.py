


def factorial(num):
    
    fact=1
    
    for i in range(1,num+1):
    
     fact=fact*i
    
       
    # print(fact)
   
    return fact
 
result=factorial(3)

print(result)




#create a function num_chk return odd if number is odd esle retun even


# def num_chk(number):
    
#     return "even" if number%2==0 else "odd"


# print(num_chk(11))





#create afunction max_num with 2 paramer num1,num2 Nand return lagest number

# def max_two(num1,num2):
    
#     return "num1" if num1>num2 else "num2"

# print(max_two(431,76))




#create a function multipliaction_table(number,n)  print multipliccation table of number till n


# def multtiplication_table(number,n):
    
    
#     for i in range(1,n+1):
        
    
#      print(f"{i} * {number} = {i*number}")
     
# multtiplication_table(3,10)






#create a function min_num with two parameter num1,num2 annd return smallest number


# def min_num(num1,num2,):
    
#     return "num1" if num1<num2 else "num2"

# print(min_num(15,8))



#create a function exponent with 2 parameter number a n
# 
# 
# def expo(number,n=3):
    
#     return number**n

# print(expo(2))


#crete a function smart_sub with 3 parameter num1,num2,reverwse

# def smart_sub(num1,num2,reverse):
    
#      return num2-num1 if reverse==True else num1-num2 
 
# print(smart_sub(2,10,True))



#create a function random_number(strt,end,step)

#print numbers from start to end
#random_nuber(1,7,2)

def random_number(start,end,step):
    
    while start<=end:
        
        print(start)
        
        start=start+step
        
random_number(1,7,2)