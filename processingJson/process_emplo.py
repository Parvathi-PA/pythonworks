from json import load

f=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\dataset\\employee.json")

data=load(f)

for emp in data:
    
    print(emp)