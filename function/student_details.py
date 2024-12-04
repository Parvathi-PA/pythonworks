
def student_details(*args,**kwargs):
    
    if kwargs.get("operation")=="total":
        
        return sum(args)
        
    
    if kwargs.get("operation")=="avg":
          
          return  sum(args)/len(args)
        
        
    
# print(student_details(45,43,55,operation="total"))
    
print(student_details(45,43,55,operation="avg"))
    
    
        
        
    
    
    
