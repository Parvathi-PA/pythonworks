
class Mobile:
    
    name:str
    
    price:int
    
    brand:str
    
    def __init__(self,name,price,brand):
        
        
        self.name=name
        
        self.price=price
        
        self.brand=brand
        
    def display(self):
        
        print(self.name,self.price,self.brand)
        
Mobile_instance=Mobile("redmi12",4500,"redmi")

Mobile_instance.display()
