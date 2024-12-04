
#
#swap elements with odd indx

arr=[10,20,30,40,50,60,70,80,90,100]
#     0  1  2  3  4  5  6  7  8  9
#        L           R  
  
left=1
right=len(arr)-1 #9-1=8

if right%2==0:
     right-=1 # right=5
    
while left<right:
    
 arr[left],arr[right]=arr[right],arr[left]
    
 left+=2
    
 right-=2
print(arr)
    
    