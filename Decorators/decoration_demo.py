
# def swap_decorator(fn):
    
#     def wrapper(n1,n2):
        
#         if n1<n2:
#             (n1,n2)=(n2,n1)
            
#         return fn(n1,n2)
        
#     return wrapper
 
# @swap_decorator    
# def smart_sub(num1,num2):
    
#     return num1-num2

# @swap_decorator
# def smart_div(num1,num2):
    
#     return num1/num2

# print(smart_sub(10,2))
# print(smart_sub(2,10))



def samrt_dec(fn):
    def wrapper(n1,n2):
        if n1<n2:
            
            (n1,n2)=(n2,n1)
            
        return fn(n1,n2)
    
    return wrapper

def round_dec(fn):
    def wrapper(n1,n2):
        
        n1=round(n1)
        n2=round(n2)

@samrt_dec

def add_num(num1,num2):
    
    return num1+num2

@samrt_dec

def substartion(num1,num2):
    
    return num1-num2

@samrt_dec

def division(num1,num2):
    
    return num1/num2

print(division(2.4,10.4))