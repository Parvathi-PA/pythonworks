

lst1=["apple","mango","onion","potatto"]

lst2=[100,200]

result={}

# result={lst1[i]:lst2[i] for i in range(len(lst2))}




for i in range(0,len(lst2)):
    lst1_index_ele=lst1[i]
    lst2_index_ele=lst2[i]
    
    result[lst1_index_ele]=lst2_index_ele
    
    balanced_lst1=lst1[len(lst2)::]

for index,element in enumerate(balanced_lst1): 

 result[element]=index+1


print(result)