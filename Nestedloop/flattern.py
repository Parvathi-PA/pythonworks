


arr=[
    [10,20],
    [20,30],
    [30,40],
    [40,50]
]

#flat the list

flat_lst=[num for lst in arr for num in lst]

print(flat_lst)