# from re import fullmatch

# date=input("entr date:")

# pattern="([1-9]|0[1-9]1[0-2])"

# matcher=fullmatch(pattern,date)

# if matcher==None:
    
#     print("invalid")
    
# else:
#     print("valid")





# from re import fullmatch

# date=input("entr date:")

# pattern="(0?[1-9]|[12][0-9]|3[01])"

# matcher=fullmatch(pattern,date)

# if matcher==None:
    
#     print("invalid")
    
# else:
#     print("valid")



from re import fullmatch

year=input("entr date:")

pattern="(18|19)[0-9]{2}|20[01][0-9]|202[0-4])"

matcher=fullmatch(pattern,year)

if matcher==None:
    
    print("invalid")
    
else:
    print("valid")