
# year=int(input("Enter the year:"))

# if (year%100!=0 and year%4==0) or (year%100==0 and year%400==0):
    
#     print("leap year")
    
# else:

#     print("not leap year")


year=int(input("entre the year:"))

is_centuary=year%100==0 and year%400==0  

print(is_centuary)


