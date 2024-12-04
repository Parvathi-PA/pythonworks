

#class list:

#  def append(self):    append is used to insert new obect to the end of the list
#   def pop()    delete element freom last of a list
#  def insert()  




colors=["red","green","black"]

# colors.append("yellow")

# print(colors)

# popped_element=colors.pop()

# print(colors)

# print(popped_element)

# colors.pop(1)

# colors.insert(0,"purple")


# print(colors)


# red_index=colors.index("red")  # return index of first occurance red

# print(red_index)

#copy

# a_color=["red","green","blue","pink","indigo"]

# b_color=a_color.copy()

# b_color.pop()

# print("acol = ",a_color)

# print("bcol = ",b_color)

# list=[4,7,2,22,34,6,71,8,5]

# list.sort()

# list.sort(reverse=True)

# print(list)





arr=[2,4,12,6,5,22,11,78,3]

search_element=int(input("enter the num:"))

arr.sort()

low=0

upp=len(arr)-1

while(low<=upp):
    
    mid=(low+upp)//2
    
    if search_element==arr[mid]:
        
        print("element found")
        
        break
    elif search_element<arr[mid]:
        upp=mid-1
        
    elif search_element>arr[mid]:
        low=mid+1
        
else:
   print("not found")
        
        
        
        
        
        