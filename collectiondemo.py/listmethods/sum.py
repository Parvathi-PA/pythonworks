
#program to count the occurance of each element in a list

list=[1,2,3,2,4,4,4,5]
count=[]

count=0

for i in range(0,len(list)-1):
    for j in range(i+1,len(list)):
    
      if list[i]==list[j]:
          count+=1
          print(count)
    













#2) sum of all elements in a list

# list=[3,5,6,8,2,9]

# sum=0

# for i in range(0,len(list)):
    
#     sum=sum+list[i]
    
# print("sum of elements =",sum)



#3) split into half

# list=[3,4,2,6,5,8,7,1]

# length=len(list)-1

# half=length//2

# half_list1=list[:half+1:]
# print(half_list1)

# half_list2=list[length:half:-1]

# print(half_list2)





#4) print even numbers in a list

# list=[1,2,3,4,5,6,7,8,9,10]

# for i in range(0,len(list)):
    
#     if list[i]%2==0:
        
#         print(list[i])


#5) reverse a list


list=[1,2,3,4,5,6,7]
    
# print(list[::-1])
        
# reversed=list.reverse()
# print(list)





#6) merge 2 list

# arr1=["red","blue","pink","rose"]

# arr=[1,12,55,4,8]

# arr2=[3,7,8,0,-1]

# arr.extend(arr2)

# arr.sort()

# print(arr)




#7) length of a list without using len()

# list=[8,6,4,9,2,3]

# length=0

# for i in list:
    
#     length=length+1
    
# print(length)

# #or

# print(len(list))


#8) python program to multiply all elemets in a list

# list=[1,2,3,4,5,6,7]

# multiply=1

# for i in list:
    
#     multiply=multiply*i
    
# print(multiply)


#9) program to replace an element in a list with another element


# arr=["red","blue","pink","rose"]

# list=[1,2,3,4,5,6,7]

# arr[0]="black"

# list[6]="rose"

# print(arr)

# print(list)


#10) program to remove an element from a list by index

# arr=["red","blue","pink","rose"]

# remove_element="red"

# arr.remove("red")

# print(arr)


#11) program to check  a list is empty

# arr=["red","blue","pink","rose"]

# # list=[]

# length=len(arr)

# if length==0:
    
#     print("empty list") 
    
# else:
#     print("not empty")


#12) program to find common elements in two list

# list1=[2,1,3,4,6]

# list2=[9,8,2,7,1]

# list1.sort()

# list2.sort()

# duplicate_list=[]

# for i in range(0,len(list1)-1):
#     for j in range(0,len(list2)-1):
        
#         if list1[j]-list2[i]==0:
            
#             duplicate_list=list2[j]          
    
#             print(duplicate_list)
            
            
            
#13) find maxmum and minimum elements of a list

# arr=[5,8,3,10,34,2,1,6,88,-1]

# print(max(arr))

# print(min(arr))


#14) program to remove  duplicate from a list

# list=[2,1,3,4,6,2,1]

# new_list=[]

# for i in range(0,len(list)):
    
#     if list[i]  not in new_list:
        
#         new_list.append(list[i])
        
# print(new_list)


# 15)find second largest element in a list

list=[2,1,8,11,4,6,7] #7

list.sort()

length=len(list)-1 #6

list.remove(list[length])#11 remove

second_largest=len(list)-1

print("second largest element=",list[second_largest])

