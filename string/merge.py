


text1="PQRST"

text2="ABC"

# result=""

# for i in range(0,len(text2)):
    
#     result+=text1[i]+text2[i]
    
# print(result)



smallest_text=min(text1,text2)


largest_text=max(text1,text2)

# print(smallest_text)


# smallest_text=text1 if text1<text2 else text2

# largest_text=text1 if text1>text2 else text2
 
result=""

for i in range(0,len(smallest_text)):
    
    result+=text1[i]+text2[i]
    
balance_text=largest_text[len(smallest_text):]

result+=balance_text

print(result)



#print first recursive text

text1="ABCABC"

recursive_text="A"


result=""

for i in range(0,len(text1)):
    
    if  text1[i]==recursive_text:
     
     #result=recursive_text    
     print(recursive_text)