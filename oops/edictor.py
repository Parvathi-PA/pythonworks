class Editor:
    
    name=str
    
    ventor=str
    
    def __init__(self,name,ventor):
        
        self.name=name
        
        self.ventor=ventor
        
        
    def __str__(self):  #object string representation
        
        return self.name
    
editor_instance=Editor("vscode","Micosoft") 

editor_instance1=Editor("intellij","jetbrains")

editor_instance2=Editor("pycharm","jebrains")

print(editor_instance1)