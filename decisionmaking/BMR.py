
weight=int(input("Enter the weight:"))

height=int(input("Enter the height:"))

Age=int(input("Enter the age:"))

Gender=int(input("""
                 choose gender:
                 press 1 for male
                 press 2 for female
                 
    """))

print(weight,height,Age,Gender)



# """
# The BMR=

# 10*weight + 6.25*height - 5*Age + 5 for male

# 10*weight + 6.25*height - 5*Age - 161 for female

# """

if Gender==1:

  BMR=10*weight + 6.25*height - 5*Age + 5
  
elif Gender ==2:
    
  BMR= 10*weight + 6.25*height - 5*Age -161
    
else:
    
    print(" *********please select valid gender**********")
    
print(BMR)

activity_level=int(input("""
select activity level
    pres 1 for sedentary
    pres 2 for lightly active
    pres 3 for moderatly active
    pres 4 for very active
    pres 5 for extra active
    
"""))

if activity_level ==1:
    
     calorie=BMR*1.2
     
elif  activity_level==2:
    
    calorie=BMR*1.375
    
elif activity_level==3:

    calorie=BMR*1.55
    
elif activity_level==4:
    
    calorie=BMR*1.725
    
elif activity_level==5:
    
    calorie=BMR*1.9
    
else:
    
    print("select valid choice for activity level************")
    
print(f"total number of calories you need inprder to maintain your current weight={calorie}")

targest_weight=int(input("enter the weight to be reduced in kg:"))

duration=int(input("enter the durasion in week:"))

# 1kg=7700 calorie

calorie_deficit=targest_weight*7700

days=duration*7

daily_calorie_deficit=calorie_deficit/days

print(daily_calorie_deficit)

total_calorie=calorie_deficit+daily_calorie_deficit

print("Total calorie after reduction:",total_calorie)