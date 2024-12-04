

employee={"eid":"ag345",
          "name":"manu",
          "salary":24000,
          "department":"hr",
          "experience":3}

print(employee["salary"])

#add contact as 3446456

employee["contact"]=3446456
# print(employee)

# if experience > 5 update employee salary as current_salary+10000 else current_salary+5000

# if employee["experience"] > 5:
    
#     employee["salary"]+=10000
    
# else:
    
#     employee["salary"]+=5000
    
# print(employee)


# add role aas SDE if exp>5 else add role as JDE

# if employee["experience"]>5:
    
#     employee["role"]="SDE"
    
# else:
#     employee["role"]="JDE"
    
# print(employee)
 
 
 
 
 
 
employee={"id":"7hhu","name":"anu","deparment":"manager","age":45,"salary":30000}

# print(employee.get("salry")) #return none if we use get()

# print("hai mam")

# #pop(key) remove key value pair

# employee.pop("salary")

# print(employee)

# #return all keys ==>keys()

# for k in employee.keys():
#     print(k)

# employee_key=employee.keys()
# print(employee_key)

# #fetch all values =>values()

# for v in employee.values():
#     print(v)
    
# employee_value=employee.values()
# print(employee_value)

#items() => for taking both keys and values

for k,v in employee.items():
    print(k,v)
    
