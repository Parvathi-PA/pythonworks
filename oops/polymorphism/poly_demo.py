
#polymorphicsm (more than one form)
#method_overloading(same method name  and different number of parameter)
#method_overriding


class Operations:
    
 def add(self,num1,num2):
    
    print(num1+num2)
    
 def add(self,num1,num2,num3):
    
    print(num1+num2+num3)
    
obj=Operations()
obj.add(10,20,30)
obj.add(10,20)

#pyhton doesnot support method overloading