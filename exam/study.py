# from flask import Flask, render_template, request, redirect, url_for
# import sqlite3

# app = Flask(_name_)

# # Create a function to connect to the database
# def connect_db():
#     return sqlite3.connect('inventory.db')

# # Create inventory table if it doesn't exist
# def create_inventory_table():
#     conn = connect_db()
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS inventory (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             item_name TEXT NOT NULL,
#             quantity INTEGER NOT NULL
#         )
#     ''')
#     conn.commit()
#     conn.close()

# # Home route to render the inventory form
# @app.route('/')
# def inventory_form():
#     return render_template('inventory.html')

# # Route to handle form submission and save the list to the database
# @app.route('/add_inventory', methods=['POST'])
# def add_inventory():
#     if request.method == 'POST':
#         items = request.form.getlist('item_name')  # List of item names from the form
#         quantities = request.form.getlist('quantity')  # List of quantities from the form

#         # Save the items to the database
#         conn = connect_db()
#         cursor = conn.cursor()

#         for item, qty in zip(items, quantities):
#             cursor.execute("INSERT INTO inventory (item_name, quantity) VALUES (?, ?)", (item, qty))

#         conn.commit()
#         conn.close()

#         return redirect(url_for('inventory_form'))

# # Run the app
# # if _name_ == '_main_':
# #     create_inventory_table()  # Ensure the table is created
# #     app.run(debug=True)


# import sqlite3

# # Define the item data structure (for this example, using a dictionary)
# inventory_items = [
#     {"item_id": 1, "name": "Widget A", "quantity": 50, "price": 19.99},
#     {"item_id": 2, "name": "Widget B", "quantity": 30, "price": 29.99},
#     {"item_id": 3, "name": "Widget C", "quantity": 20, "price": 39.99},
# ]

# # Connect to the SQLite database (or create it if it doesn't exist)
# def connect_db(db_name='inventory.db'):
#     conn = sqlite3.connect(db_name)
#     return conn

# # Create the inventory table if it doesn't exist
# def create_table(conn):
#     query = '''
#     CREATE TABLE IF NOT EXISTS inventory_items (
#         item_id INTEGER PRIMARY KEY,
#         name TEXT NOT NULL,
#         quantity INTEGER NOT NULL,
#         price REAL NOT NULL
#     );
#     '''
#     conn.execute(query)
#     conn.commit()

# # Function to insert the list of inventory items into the database
# def save_inventory_items(conn, items):
#     query = '''
#     INSERT OR REPLACE INTO inventory_items (item_id, name, quantity, price)
#     VALUES (?, ?, ?, ?)
#     '''
#     # Insert each item from the list into the database
#     for item in items:
#         conn.execute(query, (item["item_id"], item["name"], item["quantity"], item["price"]))
#     conn.commit()

# # Main function to run the saving process
# def main():
#     # Step 1: Connect to the database
#     conn = connect_db()
    
#     # Step 2: Create the inventory table (if it doesn't already exist)
#     create_table(conn)
    
#     # Step 3: Save the inventory items
#     save_inventory_items(conn, inventory_items)
    
#     # Step 4: Close the connection
#     conn.close()
#     print("Inventory items saved successfully!")

# if _name_ == "_main_":
#     main()

# from re import finditer

# text="I have 3 cars,2 bike and 1 Cycle"

# pattern="[^A-Z0-9 ,ak]"

# matcher=finditer(pattern,text)

# for m in matcher:
    
#     print(m.group())


#quantifieres


# from re import finditer

# text="aabbbababcaaa"
# # pattern="a{2}b{2}"
# pattern="a{1,3}"
 
# matcher=finditer(pattern,text)

# for obj in matcher:



    
#     print(obj.start(),obj.group())

# from re import fullmatch

# user_input=input("entr valu:")

# pattren="[a-zA-Z][a-zA-Z0-9_]*"

# matcher=fullmatch(pattren,user_input)

# if matcher==None:
    
#     print("invalid")
    
# else:
#     print("valid")


# from re import fullmatch

# user_input=input("entre pattern:")

# pattern="[p-t][369][a-zA-Z0-9]*@"

# matcher=fullmatch(pattern,user_input)

# if matcher==None:
#     print("invalid")
# else:
#     print("valid")

# from re import fullmatch

# user_input=(input("enter ph numbr:"))

# pattern="(91)?[0-9]{10}"

# matcher=fullmatch(pattern,user_input)

# if matcher==None:
    
#     print("invalid")
    
# else:
#     print("valid")

# from re import fullmatch

# user_input=input("entr value:")

# pattern="(KL)[0-9]{2}[A-Z]{1,2}[0-9]{4}"

# matcher=fullmatch(pattern,user_input)

# if matcher==None:
    
#     print("invalid")
    
# else:
#     print("valid")

# from re import fullmatch

# f=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\regularexpre_fileworks\\hashtag_file.txt")

# for line in f:
    
#     phone=line.rstrip("\n")
    
#     # words=phone.split(" ")
    
    
#     pattern="(#)+[a-zA-Z!0-9]*"
    
#     for w in words:
#      matcher=fullmatch(pattern,w)
    
#     if matcher!=None:
        
#         print(w)
        
        
# from re import finditer

# f=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\regularexpre_fileworks\\hashtag_file.txt")

# for line in f:
    
#     words=line.rstrip("\n")
    
#     pattern="#\w+"
    
#     matcher=finditer(pattern,words)
    
#     for obj in matcher:
        
#         print(obj.group())



# from re import finditer

# f=open("C:\\Users\\parva\\OneDrive\\Desktop\\pythonworks\\regularexpre_fileworks\\url_file.txt")

# content=f.read()
    
# # line=line.rstrip("\n")
    
# pattern="(http://|https://)[\w\S./]+"

# matcher=finditer(pattern,content)

# for obj in matcher:
    
#     print(obj.group())



# def product(*args):
    
#     result=1
    
#     for num in args:
        
#         result=result*num
        
#     return result
        
# print(product(2,3,5))


# def second_max(*args):
    
#     sorted_num=sorted(args,reverse=True)
    
#     return sorted_num[1]

# print(second_max(9,35,23,3,6,4,67))

# def data(**kwargs):
    
#     print(kwargs.get("age"))
    
# data(id=120,name="anu",age=45,place="kottayam")

# def calculator(*args,**kwargs):
    
#     if kwargs.get("operation")=="+":
        
#         return sum(args)
    
#     if kwargs.get("operation")=="*":
        
#         result=1
        
#         for num in args:
            
#             result=result*num
            
#         return result
    
# print(calculator(10,20,30,operation="*"))


# n1=int(input("entr n1:"))#3

# n2=int(input("entr n1:"))#0

# try:
#    result=n1/n2 #3/0 error

#    print(result)#

# except Exception as e:
    
#      print(e) #print
     
# finally:
    
#     print("file write")

#     print("file read")


# arr=[4,5,67,2,3]

# index=int(input("entr index:"))

# try:
#   print(arr[index])
  
# except:
    
#     index=int(input("entr another index"))
    
#     print(arr[index])

# print("file write")

# print("file tetsef")

# def review(rating):
    
#     if rating<0:
        
#         raise Exception ("too low")
    
#     elif rating>10:
        
#         print("too high")
        
#     else:
        
#         print("done!")
        
# try:
#     review(22)
    
# except Exception as e:
    
#     print(e)
    
# finally:
    
#     print("hello")
    
#     print("haii")



# def review(rating):
#     if rating<0:
        
#         raise Exception("too low")
#     elif rating>10:
#       raise Exception("too high")
        
#     else:
        
#         print("done!")
# try:        
#     review(6)
    
# except Exception as e:
    
#     print(e)

# finally:
    
#     print("dhhfd")
    
#     print("teyybb")


# def poll(age):
    
#     assert age>18,"invalid age"
    
#     print("voted")

# try:
#   poll(2)

# except Exception as e:
    
#     print(e)

# def leap_year(year):
    
#     if year%4==0 and year%100!=0 or  year%100==0 and year%400==0:
        
#         return True
    
# def test_leap_year():
    
#     assert leap_year(2024)==True,"non centuary year chk failed"
    
#     assert leap_year(2025)==False,"invalid non centuary chk failed"
    
#     assert leap_year(2000)==True,"centy year chk  failed"
    
#     assert leap_year(1900)==False,"invalid chenty year chk failed"
    
#     assert leap_year(-2024)==False,"invalid year chk failed"
    
# try:
#     test_leap_year()
    
#     print("test passed")
    
# except Exception as e:
    
#     print("test failed",e)
    
    
# def factorial(number):
    
#     for i in range(0,number):
        


# def swap_dec(fn):
#     def wrapper(n1,n2):
#         if n1<n2:
#             n1,n2=n2,n1
            
#         return fn(n1,n2)
#     return wrapper
 
# @swap_dec               
# def smart_sub(n1,n2):
    
#     return n1-n2

# @swap_dec
# def samrt_div(n1,n2):
    
#     return n1/n2

# print(samrt_div(2,10))
# print(smart_sub(2,10))
 
 
 
 
 
# def swap_dec(fn):
#     def wrapper(num1,num2):
#         if num1<num2:
#             num1,num2=num2,num1
#         return fn(num1,num2)     
#     return wrapper

# def round_dec(fn):
#     def wrapper(n1,n2):
#         n1=round(n1)
#         n2=round(n2)
#         return fn(n1,n2)
#     return wrapper
    
# @swap_dec
# @round_dec    
# def add_num(n1,n2):
    
#     return n1+n2

# @swap_dec
# @round_dec
# def substration(n1,n2):
    
#     return n1-n2

# @swap_dec
# @round_dec
# def div(n1,n2):
    
#     return n1/n2

# print(div(2.3,10.4))


# class Student:
    
#     name:str
    
#     id:int
    
#     age:int
    
#     course:str
    
#     def set_student(self,name,id,age,course):
        
#         self.name=name
#         self.id=id
#         self.age=age
#         self.course=course
        
#     def display(self):
        
#         print(self.name,self.age,self.id)
        
# stu_instance=Student()

# stu_instance.set_student("anu",125,12,"cse")
# stu_instance.display()

# class Movie:
    
#     title:str
    
#     rating:int
    
#     run_time:int
    
#     director:str
    
#     genre: str
    
#     def __init__(self,title,rating,run_time,director,genre):
        
#         self.title=title
#         self.rating=rating
#         self.run_time=run_time
#         self.director=directora
#         self.genre=genre
        
#     def display(self):
        
#         print(self.title,self.rating)
        
# movie_instance=Movie("kgf",4,2.4,"babu","action")
    
# movie_instance.display()   


# class Bank:
    
#     def __init__(self,acno,balance,ac_type,cust_name):
        
#         self.acno=acno
        
#         self.balance=balance
        
#         self.ac_type=ac_type
        
#         self.cust_name=cust_name
        
#     def deposite(self,amount):
        
#         self.balance+=amount
        
#         print(self.balance)
        
#     def withdraw(self,amount):
        
#         if self.balance<amount:
            
#             print("insufficient amounr")
            
#         else:
            
#             self.balance-=amount
            
#             print("balance:",self.balance)
            
#     def get_balance(self):
        
#         print(self.balance)
        
# bank_instance=Bank("hhhf364",4000,"saving","anu")

# bank_instance.deposite(100)

# bank_instance.withdraw(200)

# bank_instance.get_balance()



# class Car:
    
#     def __init__(self,name,brand,fuel_type):
        
#         self.name=name
        
#         self.brand=brand
        
#         self.fuel_type=fuel_type
        
        
#     def display(self):
            
#             print(self.name,self.brand,self.fuel_type)
            
#     def __str__(self):
            
#             return self.name
        
# car1=Car("87866","suzuki","petrol")

# car1.display()

# print(car1)


# class Editor:
    
#     def __init__(self,name,ventor):
        
#         self.name=name
#         self.ventor=ventor
    
#     def __str__(self):
        
#         return self.name

# editor=Editor("vscode","jebrains")

# editor2=Editor("intellij","jetbrains")

# editor3=Editor("oycham","hfhgh")

# print(editor)


# class Parent:
    
#     def vehicle(self):
        
#         print("parent class ertiga vehicle")
        
# class child(Parent):
    
#     pass

# child_instance=child()

# child_instance.vehicle()


# class Person:
#     name=str
#     age=int
    
#     def __init__(self,name,age):
        
#         self.name=name
#         self.age=age
        
#     def display_person_info(self):
        
#         print(self.name,self.age)
        
# class Employee():
    
#     def __init__(self,emp_id,salary):
        
#         self.emp_id=emp_id
#         self.salary=salary
        
#     def displayemp_info(self):
        
#         print(self.emp_id,self.salary)
        
# class Manager(Person,Employee):
    
#     def __init__(self,name,age,emp_id,salary,department):
        
#         Person.__init__(self,name,age)
        
#         Employee.__init__(self,emp_id,salary)

#         self.dept=department
        
#     def display_mana_info(self):
        
#         self.display_person_info()
        
#         self.displayemp_info()
        
#         print(self.dept)
        
# manader_insta=Manager("ammu",23,"6fg",40000,"hr")

# manader_insta.display_mana_info()


# class Cusine:
    
#     def __init__(self,name):
        
#         self.name=name
        
#     def diplay_cusine(self):
        
#         print(self.name)
        
# class MealType:
    
#     def __init__(self,meal_name):
        
#         self.meal_name=meal_name
        
#     def dispaly(self):
        
#         print(self.meal_name)
        
# class Dish(Cusine,MealType):
    
#     def __init__(self,name,meal_name,dsh_name):
        
#         Cusine.diplay_cusine(name)
        
#         MealType.dispaly(meal_name)
        
#         self.dsh_name=dsh_name
        
# dish=Dish("pizzza","snak","ittalian")

# dish.dispaly(de




# def is_palindrome(string):
   
#  original=string 

#  for ch in string:
     
#      if ch ==original:
         
#          return True
     
#      else:
         
#          return False
        
    
    
    
# print(is_palindrome(racecar))



# def is_palindrome(string):
    
#     reverse=string
    
#     for ch in string:
        
#         return reverse==reverse[::-1]
    
# print(is_palindrome("racecar"))


# 

# num=int(input("entr number:"))

# if num%15==0:
#     print("PINGPONG")
    
# elif num %5==0:
    
#     print("PONG")
    
# elif num%3==0:
#     print("PING")
    
# else:
#     print(num)


def is_prime(num):
    if num<=1:
        return False
    
    for i in range(2,num+1):
        
        if num%i==0:
            
            return False
    
    return True
        
# def next_prime(num):
    
#     prime=num+1
    
#     while not is_prime(prime):
        
#         prime+=1
#         return prime
        
# print(next_prime(7))


# def is_prime(n: int) -> bool:
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def next_prime(number):
#     candidate = number + 1
#     while not is_prime(candidate):
#         candidate += 1
#     return candidate

# print(next_prime(7))


text="Hello world! This is a test for finding the longest word."

words=text.split(" ")

# print(max(words,key=lambda w:len(w)))


# def max_word(text):
    
#     words=text.split(" ")
    
#     length=lambda w:len(w)
    
#     print(max(words,key=length))  
    
# max_word("Hello world! This is a test for finding the longest word.")  


# number=int(input("entr num:"))

# orinal=number
# length=len(str(number))

# total=0

# while (number!=0):
    
#     digit=number%10
    
#     exponent=digit**length
    
#     total=total+exponent
    
#     number=number//10
    
# print("armstrong number" if total ==orinal else "not armstrong")

# start=int(input("entr start:"))

# end=int(input("entr end:"))
# if start<end:
    

#   for num in range(start,end+1):
    
#     print(num)
    
# else:
#     for num in range(start,end-1,-1):
#         print(num)


# text=(input("enter string:"))

# reversed_string=""

# for i in range(len(text)-1,-1,-1):
    
#     reversed_string+=text[i]

# # print(reversed_string)

# print(text.index("e"))


# start=int(input("entr start:"))
# end=int(input("entr end:"))

# for num in range(start,end+1):
    
#     is_prime=True
#     for i in range(2,num):
        
#         if num%i==0:
            
#             is_prime=False
            
#             break
#     if is_prime==True:
#         print(num)
        
# def prime(start,end):
#     prime=[]
#     for num in range(start,end+1):
#         is_prime=True
        
#         if num<2:
#             is_prime=False
#         for i in range(2,num):
        
#          if num%i==0:
            
#             is_prime=False
            
#             break
#         if is_prime==True:
#             prime.append(num)
#     return prime
    
# print(prime(10,50))


# for row in range(1,7):
#     for sp in range(1,7-row):
        
#         print(" ",end="")
        
#     for col in range(1,row+1):
#         print("* ",end="")
#     print()  

# def cube(num):
#     result=num**3
#     print(result)
    
# cube(3)

# def sub(n1,n2):
#     result=n1-n2
#     print(result)
# sub(20,10)

# def mul(n1,n2):
#     result=n1*n2
    
#     print(result)
# mul(10,3)

# def div(n1,n2):
#     result=n1/n2
    
#     print(result)
# div(10,3)

# def max_digit(n1,n2):
    
#     n1_last_digit=n1%10
#     n2_last_digit=n2%10
    
#     print( n1 if n1_last_digit>n2_last_digit else n2)
    
# max_digit(123,561)

# max_two=lambda str1,str2:str1 if len(str1)>len(str2) else str2

# print(max_two("anu","annnu"))


# user_input=input("entr bracket")

# symbol_dictionary={
#     "{" : "}",
#     "(":")",
#     "[": "]",
#     "<":">"
# }
       
# symbol_stack=[]

# top=-1
# is_valid=True

# for symbol in user_input:
    
#     if symbol in symbol_dictionary:
        
#         top+=1
        
#         symbol_stack.append(symbol)
        
#     elif top==-1:
#         is_valid=False
        
#     elif symbol==symbol_dictionary.get(symbol_stack[top]):
#         top-=1
#         symbol_stack.pop()
        
#     else:
#         is_valid=False
        
# if len(symbol_stack)==0 and is_valid==True:
#         print("valid")
# else:
#         print("invalid")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# from re import findall

# # text="aabbagaabbbababbb"

# pattern="[a-z] [1-9]*"
# matcher=findall(pattern,text)

# for obj in matcher:
#     if matcher==None:
#         print()
#     print(obj.group())
 

user_input=input("entr pattern:")
from re import fullmatch

pattern="[a-z]*[0-9]{2}"

matcher=fullmatch(pattern,user_input) 

if matcher==None:
    print("invalid")
    
else:
    print("valid")

