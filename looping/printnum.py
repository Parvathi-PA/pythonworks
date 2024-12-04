
start=int(input("enter the start:"))

end=int(input("enter the end:"))

if start<end:
    
    for num in range(start,end+1,1):
        
        print(num)
        
else:
    
    for num in range(start,end-1,-1): #end-1 is used to include the end num we write in cse of decrement
        
        print(num)