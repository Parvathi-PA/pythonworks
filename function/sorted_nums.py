
def sorted_num(*args,**kwargs):
    
    if kwargs.get("reverse")=="True":
        
        return sorted(args,reverse=True)
        
    if kwargs.get("reverse")=="False":
        
         return sorted(args)
        
         
# print(sorted_num(1,2,6,4,15,11,reverse="True")) #descenting

print(sorted_num(1,2,6,4,15,11,reverse="False"))