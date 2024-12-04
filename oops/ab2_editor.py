from abc import ABC,abstractmethod

class Editor(ABC):
    
    @abstractmethod
    def open(self):
      pass 
  
    @abstractmethod 
    def write(self):
        pass
    
    @abstractmethod
    def debug(self):
        pass
    
    @abstractmethod
    def execute(self):
        pass
    
class Vscode(Editor):
    
    def open(self):
        
        print("open vscode")
        
    def write(self):
        print("write in vscode")
        
    def debug(self):
        print("debug code")
        
    def execute(self):
        print("code executed")
        
vscode_instance=Vscode()

vscode_instance.open()