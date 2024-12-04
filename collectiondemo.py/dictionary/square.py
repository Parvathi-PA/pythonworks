
arr=[10,20,30,40,2,3,5,7,8]

# result={}

# for num in arr:
    
#     square=num**2
    
#     result[num]=square


#dictionary compr

# result={num:num**3 for num in arr}

# print(result)


# even_square={num:num**2 for num in arr if num%2==0}

# print(even_square)

# odd_cubes={num:num**3 for num in arr if num%2!=0}
# print(odd_cubes)
# even={}
# odd={}
# for num in arr:
#     if num%2==0:
#         even[num]=num**2
#     elif num%2!=0:
#         odd[num]=num**3
# print(odd)
# print(even)


arr=[10,3,6,7,2,3,4,10,11,5,2,10]

frequesnt_count={num:arr.count(num) for num in arr}
print(frequesnt_count)