
#missing number

# arr=[1,3,5,4]

# arr.sort()

# for i in range(0,len(arr)-1):
    
#     j=i+1
    
#     result=arr[j]-arr[i]
    
#     if result!=1:
#          print(arr[i]+1)
#          break


#print duplicate number


arr=[1,2,2,2,1,4,5]

arr.sort()

duplicate_number=[]

for i in range(0,len(arr)-1):
  j=i+1
    
  result=arr[j]-arr[i] 
  
  if result==0:
        
    if arr[i] not in duplicate_number:
        
        duplicate_number.append(arr[i])
    
print(duplicate_number)



# arr=[1,2,2,2,1,4,5]

# count=0

# for i in range(0,len(arr)-1):
#     j=i+1
    
#     count+=1
    
#     if arr[i]==arr[j]:
        
#         print(arr[i])
# print(count)        