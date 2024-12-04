

arr=[2,4,8,3,1,6]

search_element=int(input("entre the num:"))

is_present=False

for i in range(0,len(arr)):
    
    if search_element==arr[i]:
        
        is_present=True
        
        break
print(is_present)