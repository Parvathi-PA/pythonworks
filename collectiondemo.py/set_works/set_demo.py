

#lst=[]
#tp=()

# set() #dict
# st=set()#set

# st={10,20,30,10,20,30,"hello","hai"}#in set duplicate is not allowed

# print(st)  # set does not support indexing,not preserve insertion order

# #methods in set

# colors={"red","green","black"}

# colors.add("yellow")

# print(colors)




st1={1,2,3}

st2={1,2,3,4,5}

# print(st1.issubset(st2))

# print(st2.issuperset(st1))


# symm_difference=(A union B)-(A^B)


symmetric_diffe=st1.symmetric_difference(st2)

# print(symmetric_diffe)



#update

# st1={1,2,3}

# st2={1,2,3,4,5}

# st1.update(st2)
# print(st1)


text="this is a test to remove dupluicate words this test is simple"

#split into words

words=text.split(" ")
print(words)

new_text=set(words)
print(new_text)

text2="this simple test remove duplicate words"
text2=set(text2)
print(text2.issubset(text))



