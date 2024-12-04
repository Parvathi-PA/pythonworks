


# arr=[10,13,15,7,5,9]

# arr1=[1,3,2,5,10,67]

# #common element print without using "in"
# count=0
 
# for i in range(0,len(arr)):
#     for j in range(0,len(arr1)):
#         count+=1
        
#         if arr[i]==arr1[j]:
            
#          print(arr[i])
         
         
         


# arr1=[1,3,4,5]

# # find least +ve missing interger 2

# # arr2=[1,2,3,5]

# for i in range (0,len(arr1)):
#     if arr[i]==2:
#         print(arr1[i])
          
        
#     else:
#         print("2")

 
 
 #common element second method
 
 
arr1=[10,12,11,14,15,16]

arr2=[11,13,14,15,16]

arr1.sort()

arr2.sort()

p1=0
p2=0

while(p1<len(arr1) and p2<len(arr2)):
    if arr1[p1]==arr2[p2]:
        
        print(arr1[p1])
        
        p1+=1
        
        p2+=1
        
    elif arr1[p1]<arr2[p2]:
         
         p1+=1
         
    elif arr1[p1]>arr2[p2]:
        
        p2+=1