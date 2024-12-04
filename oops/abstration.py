

from abc import ABC,abstractmethod

class Bike(ABC):
    
    @abstractmethod
    
    def start(self):
        pass
    
    @abstractmethod
    def acceralate(self):
        pass
    
    @abstractmethod
    def stop(self):
        
        pass
    
class Hunter(Bike):
    
    def start(self):
        print("hunter start method")
        
    def acceralate(self):
            print("hunter accelarate")
            
    def stop(self):
         print("hunter stop")
         
hunter_instance=Hunter()

hunter_instance.start()

hunter_instance.acceralate()

hunter_instance.stop()
            
            
    
    