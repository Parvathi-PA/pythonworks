
#program for calculating BMI

#BMI = weight in kg/height in metre**2

weight_in_kg = int(input("Enter the weigh:"))

height_in_cm = int(input("Enter_the_height:"))

height_in_metre = height_in_cm/100

BMI = weight_in_kg/height_in_metre**2

BMI=round(BMI,2)

print(f"BMI is {BMI}")