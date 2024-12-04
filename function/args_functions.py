

# def add_num(*args):
    
#     print(args)
    
# add_num(10,20)

# add_num(10,20,30,40)


# def product(*args):
    
#     result=1
    
#     for num in args:
        
#         result=result*num
        
#         return result
    
# print(product(10,20))


#create a function that accept any number of arguments and return  second maximum number


def second_maxnum(*args):
    
    sorted_numbers=sorted(args,reverse=True)
    
    return sorted_numbers[1]

print("second lagest  number:",second_maxnum(35,12,4,67,45))