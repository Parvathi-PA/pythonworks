

class Cusine:
    
    def __init__(self,name):
        
        self.name=name
        
    def diplay_cusine(self):
        
        print(self.name)
        
class MealType:
    
    def __init__(self,meal_name):
        
        self.meal_name=meal_name
        
    def display_mealtype(self):
        
        print(self.meal_name)
        
class Dish(Cusine,MealType):
    
    def __init__(self,name,meal_name,dish_name):
        
        Cusine.__init__(self,name)
        
        MealType.__init__(self,meal_name)
        
        self.dish_name=dish_name
        
    def diplay_dish_type(self):
        
        self.diplay_cusine()
        
        self.display_mealtype()
        
        print(self.dish_name)
dish_instance=Dish("italian","dinner","pizza")

dish_instance.diplay_dish_type()       