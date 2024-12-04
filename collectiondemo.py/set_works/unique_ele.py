
arr=[10,10,20,30,40,30,50]
#create empty set

st=set()

#fetch numbers from array

for num in arr:
    
    #add num to set
    
    st.add(num)
    
    #display set
# print(st)


#intersection of 2 sets

set1={10,20,30,40,50}

set2={45,10,67,20,30,89}

set1.remove(50)

print(set1)
intersect_set=set1.intersection(set2)

# print(intersect_set)

# union_st=set1.union(set2)

# print(set1.union(set2))

# print(union_st)

#difference

differnce=set1.difference(set2)

# print(set2.difference(set1))

# print(differnce)