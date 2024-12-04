
class Animal:
    
    def __init__(self,name,species):
        
        self.name=name
        
        self.species=species
        
    def __str__(self):
        
        return self.name
    
class Cat(Animal):
    
    def __init__(self, name, species):
        super().__init__(name,species)
    
    
    def sound(self):
        
        print("gawooooo")
        
class Lion(Animal):
    
    def __init__(self, name, species):
        super().__init__(name, species)
        
    def sound(self):
        
        print("roarr")
        
# cat_instance=Cat("cat","felis catus")

# cat_instance.sound(
    
lion_instance=Lion("lion","carnivors")

print(lion_instance)

#str method used for string representation of object