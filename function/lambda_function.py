#lambda function

def add(n1,n2):
    return n1+n2
# print(add(10,20))

#we can reducd normal function into a single line by using lambda function
#we can write lambda fun only for a single line of code 

#lambda function for add 2 nums

add=lambda n1,n2:n1+n2

# print(add(20,30))

#cube

cubes=lambda n:n**3

# print(cubes(3))

#substraction

sub=lambda n1,n2:n1-n2
# print(sub(100,50))


max_two=lambda str1,str2:str1 if len(str1) > len(str2) else str2

# print(max_two("and","ammma"))

min_two=lambda str1,str2:str1 if len(str1) < len(str2) else str2

# print(min_two("and","ammma"))

#

def smart_sub(n1,n2):
    return n1-n2 if n1>n2 else n2-n1

#reduced as

smart_sub=lambda n1,n2: n1-n2 if n1>n2 else n2-n1
# print(smart_sub(20,100))

words=["hello","hai","morning","test","apple"]

# def get_length(words):
    
#     return len(words)

#          or

get_length=lambda x:len(x)

#    or

print(max(words,key=get_length))