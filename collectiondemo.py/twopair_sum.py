

# arr=[2,3,4,5]

# sum=8

# for i in range(0,len(arr)-1):
    
#     for j in range(i+1,len(arr)):
    
#      if arr[i]+arr[j]==sum:
        
#         print((arr[i],arr[j]))
        
#         break


lst=[2,3,4,5,7,8,9]

left=0

right=len(lst)-1

sum=8

while(left<right):
    
    cur_sum=lst[left]+lst[right]
     
    if cur_sum==sum:
        
        print((lst[left],lst[right]))
        
        break
    
    elif cur_sum>sum:
        
        right=right-1
        
    elif cur_sum<sum:
        
        left=left+1
        
        