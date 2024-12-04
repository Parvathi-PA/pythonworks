#1) Create a dictionary to store the names and ages of 5 people.
# Access and print the age of one person using their name

# peoples={"anu":23,"appu":12,"malu":34,"manu":44,"sanju":33}

# print(peoples["anu"])


#2) Write a Python program to merge two dictionaries

# dt1={"a":1,"b":2,"c":3,"d":4}
# dt2={"w":9,"s":8,"r":7,"t":6}
# dt1.update(dt2)
# print(dt1)

#3) Given a dictionary where the keys are student names and the values are their scores, write a program to calculate the average score

# students={"amlu":98,"sankar":77,"jency":89,"miya":90,"sree":67}
# sum=0
 
# for v in students.values():
   
#    sum=sum+v

# average=sum//len(students)
   
# print(average)


#4) Write a dictionary comprehension to create a dictionary where the keys are numbers from 1 to 10 and the values are the squares of those number

# numbers=[1,2,3,4,5,6,7,8,9,10]

# squares={num:num**2 for num in numbers}
# print(squares)


#5) Write a Python program to create a dictionary from a list of keys and values using dictionary comprehension.

lst1=["a","b","c","d"]

lst2=[10,20,30,40]

result_dict={lst1[i]:lst2[i] for i in range(len(lst1))}

print(result_dict)
















#6) Given two lists, one with fruits and the other with prices, write a dictionary comprehension to pair them together into a dictionary

# fruits=["apple","mango","orange","grape"]

# price=[25,40,56,78]

# result={ fruits[i]:price[i] for i in range(len(fruits))}
# print("result = ",result)


# 7)Write a Python program to filter a dictionary, keeping only items with values greater than 50 using dictionary comprehension

# dict={"pen":20,"book":55,"lap":1200,"bottle":45,"bag":234}

# result={k:v for k,v in dict.items() if v>50}
# print("result = ",result)


#8)Given a sentence, count the frequency of each word using a dictionary.
 

# text="this is a small village of this is a to count to"

# words=text.split(" ")

# frequency_count={}
# for w in words:
    
#     if w in frequency_count:
#         frequency_count[w]+=1
#     else:
#         frequency_count[w]=1
# print(frequency_count) 



#9) Write a dictionary comprehension to convert all the values in a dictionary to their absolute values.

# dict={"a":1,"b":-2,"c":-3,"d":-8}

# absolute_value={k:v*-1 if v<0 else v  for k,v in dict.items()}
# print(absolute_value)


# 10)Given a dictionary of items and their prices, write a program to apply a 10% discount to all the items using dictionary comprehension.

# lst={"pen":20,"book":25,"chair":234,"bag":500}

# result={k:v*.9 for k,v in lst.items()}
# print(result)