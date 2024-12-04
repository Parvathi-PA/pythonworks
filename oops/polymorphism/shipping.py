
class Shipping:
    
    def  calculate_shipping_cost(self,weight):
        
        print(weight*5)
        
class ExpressShipping(Shipping):
    
    def calculate_shipping_cost(self, weight):
         
         print(weight*20)
         
class StandShipping(Shipping):
    
    def calculate_shipping_cost(self, weight):
        
        print(weight*10)
        
standShipping_instance=StandShipping()

standShipping_instance.calculate_shipping_cost(5)

ExpressShipping_instance=ExpressShipping()

shipping_instance=Shipping()

ExpressShipping_instance.calculate_shipping_cost(5)

shipping_instance.calculate_shipping_cost(5)