

text=input("entre the string:")

# reverse_text=text[::-1]

# print("palindrome" if text==reverse_text else "not palindrome")

#text="palindrome"

length=len(text)-1 #10-9

reverse=""

for i in range(length,-1,-1):
    
     reverse+=text[i]
     
print(reverse)    