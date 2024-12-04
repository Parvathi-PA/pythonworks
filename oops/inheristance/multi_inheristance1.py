

class Person:
    
    def __init__(self,name,age):
        
        self.name=name
        
        self.age=age
        
    def display_person_info(self):
        
        print(self.name,self.age)
        
class Employee:
    
    def __init__(self,emp_id,salary):
        
        self.emp_id=emp_id
        
        self.salary=salary
        
    def displayemp_info(self):
        
        print(self.emp_id,self.salary)
        
class Manager(Person,Employee):
    
    def __init__(self, name, age,emp_id,salary,deparment):
        
        Person.__init__(self,age,name)
        
        Employee.__init__(self,emp_id,salary)   
        
        self.deparment=deparment
        
    def display_manager_info(self):     
         
         self.display_person_info()
         
         self.displayemp_info()
         
         print(self.deparment)
         
Manager_instance=Manager(33,"manu","id43",23000,"hr")

Manager_instance.display_manager_info()