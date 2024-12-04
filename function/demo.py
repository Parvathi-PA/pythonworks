


def sum(num1,num2):
    
    result=num1+num2
    
    print(result)
    
sum(100,200)


def print_course_deatils(couse_name,company_name):
    
    print(company_name)
    
    print(couse_name)
    
print_course_deatils("django","luminar")




# create a function last_digit_max with 2 para num1,num2



def last_digit_max(num1,num2):
    
    result=num1%10 or num2%10
    

    
    print("num1" if num1%10>num2%10 else "num2")
    
last_digit_max(129,238)





def last_digit_max(num1,num2):
    
     result=num1 if num1%10>num2%10 else num2 
     
     print(result)
     
last_digit_max(275,564)


