
# from re import finditer

# text="fatcatrunsveryfasttocaththerat"

# pattern="at"

# match=finditer(pattern,text)

# for m in match:
    
#     print(m.start(),m.group())


# digit count

from re import finditer

# text="I have 3 cars,2 bike and 1 Cycle"

# # pattern="[a-zA-Z]"   chk for alphanumeric
# # pattern="[0-9]"  chk for digits
# # pattern="[^ak]"  #exclude a,k
# # pattern="[^ak0-9A-Z, ]"  exclude all the mentioned
# # pattern="[^a-z0-9A-Z]" #chk special character
# # pattern="\w"#[a-zA-Z0-9] alphanumeric
# # pattern="\d"  #[0-9]
# # pattern="\D"  #exclude digits
# # pattern="\W" #special character[^a-za-Z0-9]
# # pattern="\s" #space
# # pattern="\S" #exclude space
# pattern="\w+"

# match=finditer(pattern,text)

# for d in match:
#    print(d.start(),d.group())



#Quantifiers

from re import finditer

text="ababbbbacaaaabbbaa"

# pattern="a{2}" 2a
pattern="a{1,2}" #minimum 1a and max 2a


matcher=finditer(pattern,text)

for obj in matcher:
   print(obj.start(),obj.group())